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
            
            resp = DevScan(s_ip, s_comm, s_pass, s_maker)

            # Create a list of the neighboring devices' IPs
            try:
                dev_list = list()
                for dev in resp:
                    if 'Switch has no IP adress' in dev[0]:
                        dev_list.append('0.0.0.0')
                    else:
                        dev_list.append(dev[0])
            except:
                dev_list = 'No leaf.'

            request.session['adj_devices'] = dev_list
            request.session['full_list'] = resp
            return render(request, 'answer.html', {'resp' : resp, 'dev_list': dev_list, 'dev_ip': s_ip})
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
        resp = request.session.get('full_list')
        # Create a list to put in the results from each device.
        devices = resp
        for s_ip in dev_list:
            if s_ip != '0.0.0.0':
                try:
                    device = [('Device IP Address', 'Device Name', 'Local Interface', 'Remote interface')]
                    device = device + DevScan(s_ip)
                    devices = devices + device
                    #resp = resp + [('Device', 'with', 'IP', s_ip)] + DevScan(s_ip)
                except:
                    resp = resp + [('Device', s_ip, 'failed', 'miserably')]
    else:
        return render(request, 'scan.html', {'form': SwitchForm(), 'x': x})
    return HttpResponse(devices)
    #return render(request, 'answer.html', {'resp' : resp, 'dev_list': dev_list, 'dev_ip': s_ip})


def myjson(request):
    import corestuff.myjson
    return HttpResponse(data)
