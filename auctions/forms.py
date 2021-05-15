'''from django import forms
from .models import *

class ListingForm(forms.Form):
    listtitle = forms.CharField(label='', max_length=200, required=True, widget=forms.TextInput(attrs={
        "class" : "form-control"
    }))'''