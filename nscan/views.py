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
            
            resp = DevScan(s_maker, s_ip, s_comm, s_pass)

            try:
                dev_list = list()
                for dev in resp:
                    if 'Switch has no IP adress' in dev[0]:
                        dev_list.append('0.0.0.0')
                    else:
                        dev_list.append(dev[0])
            except:
                dev_list = 'No leaf.'
                
                
            return render(request, 'answer.html', {'resp' : resp, 'dev_list': dev_list})
        else:
            return HttpResponse('Go back and fill that form like a good girl...')
        pass
    else:
        return render(request, 'scan.html', {'form': SwitchForm()})