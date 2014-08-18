#from django.shortcuts import render
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

# Create your views here.

class SwitchForm(forms.Form):
    switch_name = forms.GenericIPAddressField(
                                  label = 'Switch IP address (v4 or v6)',
                                  required = True,
                                  max_length = 41
    )
    
    snmp_community = forms.CharField(
                                     label = 'SNMP community with CDP access',
                                     required = True,
                                     max_length = 64,
                                     initial = 'public',
    )
    
    snmp_pass = forms.CharField(
                                label = 'SNMP community password',
                                required = False,
    )
    
    def __init__(self, *args, **kwargs):
        super(SwitchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
                                    'switch_name',
                                    'snmp_community',
                                    'snmp_pass',
                                    StrictButton('Go!!!', css_class='btn-default'),
        )

    
def scan(request):
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.isvalid():
            return HttpResponse('/thanks/')
        pass
    else:
        return render_to_response('scan.html', {'form': SwitchForm()}, context_instance = RequestContext(request))
        #return render(request, 'scan.html', {'form': ExampleForm()})