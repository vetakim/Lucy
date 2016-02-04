from django.forms import FloatField, BooleanField, IntegerField
from django import forms

class CalcParams(forms.Form):
    amplitude = FloatField(label="Amplitude",
            widget=forms.TextInput(attrs={'class': 'amp', 'type':
                'number', 'style': 'top: 10%', 'step': '1e-6'}))
    samples = IntegerField(label="Samples",
                widget=forms.TextInput(attrs={'class': 'amp', 'type':
                    'number', 'style': 'top: 15%'}))
    toclear = BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'cle',
        'type': 'submit', 'value': 'Clear DB', 'style': 'top: 25%'}))

