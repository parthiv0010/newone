from django import forms
from . models import *
class DestForm(forms.ModelForm):
    class Meta:
        model = Destinations
        exclude = ['creator','Reviews']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']  # Include fields you want to be editable