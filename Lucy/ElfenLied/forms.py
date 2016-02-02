from django.forms import FloatField, BooleanField
from django import forms

class CalcParams(forms.Form):
    amplitude = FloatField(label="Amplitude",
            widget=forms.TextInput(attrs={'class': 'amp', 'type': 'number'}))
    toclear = BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'cle',
        'type': 'submit', 'value': 'Clear DB'}))

