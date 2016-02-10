from django.forms import *
from django import forms
from .models import Point, RequisitionModel
from priority.scheduler import laws

class CalcClear(forms.Form):

    launch = BooleanField(required=False, label='Calculate',widget=forms.CheckboxInput(attrs={
        'style': 'top: 5%; left: 20%', 'class': 'ccinput'}))


    toclear = BooleanField(required=False, label='',widget=forms.TextInput(attrs={
        'type': 'submit', 'value': 'Clear DB', 'style': 'top: 15%',
        'class': 'ccinput'}))


class PointParams(forms.Form):
    amplitude = FloatField(label="Amplitude",
            widget=forms.TextInput(attrs={'type':
                'number', 'class': 'parinput', 'style': 'top: 5%', 'step': '1e-6'}))

    samples = IntegerField(label="Samples",
                widget=forms.TextInput(attrs={'type':
                    'number', 'class': 'parinput', 'style': 'top: 25%'}))
    choose_x_points = ChoiceField(required=False, label='x-axis',
            choices=Point.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 10%'}))

    choose_y_points = ChoiceField(required=False, label='y-axis',
            choices=Point.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 15%'}))


class ReqParams(forms.Form):
    maxtact = IntegerField(
            label="Tacts number",
            min_value=1,
            max_value=95,
            widget=forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'parinput',
                    'style': 'top: 5%'}))

    lawstring = ChoiceField(
            required=False,
            label='Decreasing law',
            choices=tuple((j, j) for j in laws),
            widget=forms.Select(attrs={'style': 'top: 15%'}))

    free_resource = FloatField(
            label="Free resource, %",
            widget=forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'parinput',
                    'style': 'top: 25%',
                    'step': '1e-6'}))

    medium = FloatField(
            label="Medium",
            widget=forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'parinput',
                    'style': 'top: 35%',
                    'step': '1e-6'}))

    dispersion = FloatField(
            label="Dispersion",
            widget=forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'parinput',
                    'style': 'top: 45%',
                    'step': '1e-6'}))

    choose_x_points = ChoiceField(
            required=False,
            label='x-axis',
            choices=RequisitionModel.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 55%'}))


    choose_y_points = ChoiceField(required=False,
            label='y-axis',
            choices=RequisitionModel.CHOICES,
            widget=forms.Select(attrs={'style': 'top: 65%'}))

