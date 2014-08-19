from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from nscan.forms import SwitchForm
# Create your views here.

    
def scan(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        #if form.isvalid():
        return HttpResponse('/thanks/')
        #pass
    else:
        return render_to_response('scan.html', {'form': SwitchForm()}, context_instance = RequestContext(request))
        #return render(request, 'scan.html', {'form': ExampleForm()})