from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class SwitchForm(forms.Form):
    switch_make = forms.ChoiceField(
                                  label = 'Manufacturer',
                                  required = True,
                                  initial = 'cisco',
                                  choices = [('cisco', 'CISCO')]
                                  )

    switch_name = forms.GenericIPAddressField(
                                  label = 'Switch IP address (v4 or v6)',
                                  required = True,
                                  max_length = 41
    )
    
    snmp_community = forms.CharField(
                                     label = 'SNMP community with read access',
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
        self.helper.form_method = 'post'
        self.helper.form_action = '/switchscan/'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
                                    'switch_make',
                                    'switch_name',
                                    'snmp_community',
                                    'snmp_pass',
                                    #StrictButton('Go!!!', name='go', value='go', css_class='btn-default'),
        )

