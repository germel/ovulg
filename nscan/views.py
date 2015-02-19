from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.core import serializers

from nscan.forms import SwitchForm # The form to fill in the switch data
from corestuff.core import DevScan
import socket # jsonify must be able to test a field
import json
import math

# Create your views here.

def scan(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.is_valid():
            s_maker = form.cleaned_data['switch_make']
            s_ip = form.cleaned_data['switch_name']
            s_comm = form.cleaned_data['snmp_community']
            s_pass = form.cleaned_data['snmp_pass']
            
            resp = [DevScan(s_ip, s_comm, s_pass, s_maker)]

            # Create a list of the neighboring devices' IPs (dev_list)
            # resp[] as of now has just one member, so it's resp[0]
            try:
                dev_list = list()
                #a = resp[0]
                if len(resp[0]) > 1:
                    for dev in resp[0]:
                        if 'Switch has no IP adress' in dev[0]:
                            dev_list.append('0.0.0.0')
                        else:
                            dev_list.append(dev[0])
            except:
                dev_list = 'No leaf.'

            # Put a header for the table in the list
            full_list = list()
            full_list.append(list([s_ip]) + list(resp)) # THE session variable to keep
            request.session['full_list'] = full_list
            request.session['adj_devices'] = dev_list
            request.session['DevScanParameters'] = [s_ip, s_comm, s_pass, s_maker]
            request.session.set_expiry(3600)
            # answer.html expects a triple nested list of lists, so resp becomes [resp]
            return render(request, 'answer.html', {'dev_list': dev_list, 'devscan': full_list})
        else:
            return HttpResponse('Go back and fill that form like a good girl...')
        pass
    else:
        return render(request, 'scan.html', {'form': SwitchForm()})

def rec_search(request): # Recursive search in the results of the first pass
    if request.session.get('adj_devices'):
        dev_list = request.session.get('adj_devices')
        devscan_parameters = request.session.get('DevScanParameters')
        full_list = request.session.get('full_list')

        try:
            s_ip, s_comm, s_pass, s_maker = devscan_parameters
        except:
            return HttpResponse('oh shit... view "rec_search" failed.')

        for s_ip in dev_list:
            if s_ip != '0.0.0.0':
                try:
                    devscan = [DevScan(s_ip)]
                    full_list.append(list([s_ip]) + list(devscan))
                except:
                    full_list.append([(s_ip, 'Device', 'failed', 'miserably')])
    else:
        return render(request, 'scan.html', {'form': SwitchForm()})
    #return HttpResponse(devices)
    request.session['full_list'] = full_list
    return render(request, 'answer.html', {'dev_list': dev_list, 'devscan': full_list})

def mapify(request):
    if 'devs' in request.path[-5:] and request.session['full_list']:
        #xx='{ "nodes": [ { "id": "n0", "label": "A node", "x": 0, "y": 0, "size": 3 }, { "id": "n1", "label": "Another node", "x": 3, "y": 1, "size": 2 }, { "id": "n2", "label": "And a last one", "x": 1, "y": 3, "size": 1 } ], "edges": [ { "id": "e0", "source": "n0", "target": "n1" }, { "id": "e1", "source": "n1", "target": "n2" }, { "id": "e2", "source": "n2", "target": "n0" } ] }'
        #return HttpResponse(request.session['jsondata'])
        return HttpResponse(sigmafy(request.session['full_list']))

    try:
        data = request.session.get('full_list')
        try:
            jsondata = jsonify(data)
        except:
            #jsondata = 'We fucked up, mate...'
            jsondata = sys.exc_info()
    except:
        try:
            jsondata += 'No jsondata'
        except:
            jsondata = 'I have no data to display.'

    request.session['jsondata'] = jsondata
    #return render(request, 'mapify.html', {'jsondata': jsondata})
    return render(request, 'mapify.html')

def jsonify(data):
    dev = '{"devices":['
    try:
        for i in data:
            dev += '{"device":"' + str(i[0]) + '","neighbors":['
            for j in i[1]:
                dev += '{"device_ip":"' + str(j[0]) + '","device_name":"' + j[1] + '","local_if":"' + str(j[2]) + '","remote_if":"' + str(j[3]) + '"},'
            dev += ']},'
    except:
        jdata = 'The error is... ' + str(data[0])
    
    dev += ']}'
    jdata = dev.replace('},]', '}]').replace('},}', '}}')

    return jdata
    #return 'Reached the end!!!'

def sigmafy(data, x=0, y=0):
    try: mynodes    # this is what is finally returned to calling function
    except: mynodes = {'nodes': [], 'edges': []}
    t = 0   # a variable to enumerate the id's for sigma.js
    tsls, tslt = [], [] # source and target lists of switches
    zuk = [] # a temp list to store ip pairs of interconnected switches
    c = 0
    for i in data:
        #if i[0] in tsls: continue
        #if x != 0 : x += 1
        if type(i[1]) == list:
            #c = x + len(i[1]) / 2   # c -> linear center for placement of source switch
            p = math.pi / (len(i[1])+1) # p -> degrees between points on half-circle for target switches
        idSource = 'n' + str(t)
        label = i[0]
        #mynodes['nodes'].append({"id" : idSource, "label": label, "x": c, "y": y, "size": 3}) #linear
        if len(zuk) > 1:
            for k in zuk:
                print("label and k in zuk are %s, %s" % (label, k))
                if label in k:
                    print("FOUND source in list -> %s, %s" % (label, k))
                else:
                    print("label not in zuk, append node %s, -> %s, t=%d" % (idSource, label, t))
                    mynodes['nodes'].append({"id" : idSource, "label": label, "x": c, "y": y, "size": 3}) #circular
                    break
        else:
            print("FIRST label in zuk, continuing")
            mynodes['nodes'].append({"id" : idSource, "label": label, "x": c, "y": y, "size": 3}) #circular
        t += 1
        tsls.append(label)
        if type(i[1]) == list:
            z = 1 # counter for placing the points on the circumference
            #y += 1
            for j in i[1]:
                #if j[0] in tslt: continue   # if there are two links between two switches, draw only one
                if (i[0], j[0]) in zuk or (j[0], i[0]) in zuk:
                    print('Stumbled on existing couple [%s, %s], node %s' % (i[0], j[0], 'n'+str(t)))
                    continue 
                x = c + math.cos(z * p)
                y =     math.sin(z * p)
                #print("x, y, p, p' z = %f %f %f %f %d\n" % (x, y, p, (z * p), z))
                mynodes['nodes'].append({"id": 'n' + str(t), "label": j[0], "x": x, "y": y, "size": 1})
                mynodes['edges'].append({"id": 'e' + str(t), "source": idSource, "target": 'n' + str(t)})
                t += 1
                z += 1
                #x += 1
                zuk.append((i[0], j[0]))
                print('Couple not found, append [%s, %s] as node %s' % (i[0], j[0], 'n'+str(t)))
                tslt.append(j[0])
            c += 2
        else:
            continue
    #print(zuk)
    sdata = json.dumps(mynodes)
    
    return sdata