from django import forms
from . models import *
class DestForm(forms.ModelForm):
    class Meta:
        model = Destinations
        fields= "__all__"