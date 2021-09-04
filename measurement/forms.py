from django import forms
from .models import *
class measurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('destination',)