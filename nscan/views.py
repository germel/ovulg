from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from nscan.forms import SwitchForm # The form to fill in the switch data
from corestuff.core import DevScan

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
                if len(resp[0]) > 1:
                    for dev in resp[0]:
                        if 'Switch has no IP adress' in dev[0]:
                            dev_list.append('0.0.0.0')
                        else:
                            dev_list.append(dev[0])
            except:
                dev_list = 'No leaf.'

            # Put a header for the table in the list
            resp.insert(0, ['Device IP Address', 'Device Name', 'Local Interface', 'Remote interface'])
            resp.insert(0, [s_ip, None, None, None])
            request.session['adj_devices'] = dev_list
            request.session['full_list'] = resp
            request.session.set_expiry(1800)
            # answer.html expects a triple nested list of lists, so resp becomes [resp]
            return render(request, 'answer.html', {'devices' : [resp], 'dev_list': dev_list, 'dev_ip': s_ip})
        else:
            return HttpResponse('Go back and fill that form like a good girl...')
        pass
    else:
        # x is a test for d3js and can be discarded.
        x='''<script type="text/javascript> 
            var rectDemo = d3.select("#rect-demo")
                .append("svg:svg")
                .attr("width", 400)
                .attr("height", 300);
            rectDemo.append("svg:rect")
                .attr("x", 100)
                .attr("y", 100)
                .attr("height", 100)
                .attr("width", 200);
            </script>'''
        return render(request, 'scan.html', {'form': SwitchForm(), 'x': x})

def rec_search(request): # Recursive search in the results of the first pass
    if request.session.get('adj_devices'):
        dev_list = request.session.get('adj_devices')
        resp = [request.session.get('full_list')]
        #devices = list()
        for s_ip in dev_list:
            if s_ip != '0.0.0.0':
                try:
                    # device[0] -> Device IP address list
                    # device[1] -> Table heading list
                    # device[2] -> List of DevScan() results 
                    device = [[s_ip, None, None, None ]]
                    device.append(['Device IP Address', 'Device Name', 'Local Interface', 'Remote interface'])
                    device.append(DevScan(s_ip))
                    resp.append(device)
                except:
                    resp.append([('Device', s_ip, 'failed', 'miserably')])
    else:
        return render(request, 'scan.html', {'form': SwitchForm()})
    #return HttpResponse(devices)
    #request.session['full_list'] = resp
    return render(request, 'answer.html', {'dev_list': dev_list, 'devices': resp})


def myjson(request):
    import corestuff.myjson
    return HttpResponse(data)
