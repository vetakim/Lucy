from django.forms import *
from django import forms
from .models import Point
from priority.scheduler import laws

class CalcClear(forms.Form):

    launch = BooleanField(required=False, label='Calculate',widget=forms.CheckboxInput(attrs={
        'style': 'top: 5%; left: 30%'}))

    choose_x_points = ChoiceField(required=False, label='x-axis',
            choices=Point.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 10%'}))

    choose_y_points = ChoiceField(required=False, label='y-axis',
            choices=Point.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 15%'}))

    toclear = BooleanField(required=False, label='',widget=forms.TextInput(attrs={
        'type': 'submit', 'value': 'Clear DB', 'style': 'top: 20%'}))

class PointParams(forms.Form):
    amplitude = FloatField(label="Amplitude",
            widget=forms.TextInput(attrs={'type':
                'number', 'class': 'parinput', 'style': 'top: 5%', 'step': '1e-6'}))

    samples = IntegerField(label="Samples",
                widget=forms.TextInput(attrs={'type':
                    'number', 'class': 'parinput', 'style': 'top: 25%'}))


class ReqParams(forms.Form):
    maxtact = IntegerField(label="Tacts",
                widget=forms.TextInput(attrs={'type':
                    'number', 'class': 'parinput', 'style': 'top: 5%'}))

    choose_y_points = ChoiceField(required=False, label='lawstring',
            choices=tuple((j, j) for j in laws),
            widget=forms.Select(attrs={'style': 'top: 25%'}))

