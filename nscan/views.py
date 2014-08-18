#from django.shortcuts import render
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

# Create your views here.

def scan(request):
    return render_to_response('scan.html', context_instance = RequestContext(request))