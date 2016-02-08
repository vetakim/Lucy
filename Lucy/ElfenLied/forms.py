from django.forms import *
from django import forms
from .models import Point

class CalcParams(forms.Form):

    amplitude = FloatField(label="Amplitude",
            widget=forms.TextInput(attrs={'class': 'amp', 'type':
                'number', 'style': 'top: 5%', 'step': '1e-6'}))

    samples = IntegerField(label="Samples",
                widget=forms.TextInput(attrs={'class': 'amp', 'type':
                    'number', 'style': 'top: 10%'}))

    launch = BooleanField(required=False, label='',widget=forms.TextInput(attrs={'class': 'cle',
        'type': 'submit', 'value': 'Calculate', 'style': 'top: 15%'}))

    toclear = BooleanField(required=False, label='',widget=forms.TextInput(attrs={'class': 'cle',
        'type': 'submit', 'value': 'Clear DB', 'style': 'top: 20%'}))

    choose_points = ChoiceField(required=False, label='Y',
            choices=Point.CHOICES,
            widget=forms.Select(attrs={'class': 'cle', 'style': 'top: 25%'}))
