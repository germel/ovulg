from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from nscan.forms import SwitchForm
from corestuff.core import CiscoScan
# Create your views here.

    
def scan(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.is_valid():
            s_ip = form.cleaned_data['switch_name']
            s_comm = form.cleaned_data['snmp_community']
            s_pass = form.cleaned_data['snmp_pass']
            resp = CiscoScan(s_ip, s_comm, s_pass)
            return HttpResponse(resp)
        else:
            return HttpResponse('/no, thanks/')
        pass
    else:
        return render_to_response('scan.html', {'form': SwitchForm()}, context_instance = RequestContext(request))
        #return render(request, 'scan.html', {'form': ExampleForm()})

