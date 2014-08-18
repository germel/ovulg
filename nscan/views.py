#from django.shortcuts import render
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from django import forms

from crispy_forms.helper import FormHelper

# Test class from the online example
class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    
# Create your views here.

def scan(request):
    #return render_to_response('scan.html', context_instance = RequestContext(request))
    return render(request, 'scan.html', {'form': ExampleForm()})