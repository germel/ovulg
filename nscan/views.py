from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from nscan.forms import SwitchForm # The form to fill in the switch data
from corestuff.core import CiscoScan
from corestuff.untangle import uCisco
# Create your views here.

def scan(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.is_valid():
            s_ip = form.cleaned_data['switch_name']
            s_comm = form.cleaned_data['snmp_community']
            s_pass = form.cleaned_data['snmp_pass']
            resp = uCisco(CiscoScan(s_ip, s_comm, s_pass))
            return HttpResponse(resp)
        else:
            return HttpResponse('Go back and fill that form like a good girl...')
        pass
    else:
        return render_to_response('scan.html', {'form': SwitchForm()}, context_instance = RequestContext(request))
        #return render(request, 'scan.html', {'form': ExampleForm()})

