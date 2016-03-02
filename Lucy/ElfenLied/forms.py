from django.forms import *
from django import forms
from .models import *
from priority.scheduler import laws, planner
from priority.sharetools import column

modeloutput = RequisitionOutput
modelinput = RequisitionInput
calcfunc = planner

class CalcClear(forms.Form):

    launch = BooleanField(required=False, label='Calculate')

    toclear = BooleanField(required=False, label='',
            widget=forms.TextInput(attrs={
                'type': 'submit', 'value': 'Clear DB' }))

    # choose_x_points = ChoiceField(
            # required=False,
            # label='x-axis',
            # choices=modeloutput.CHOICES)

    # choose_y_points = ChoiceField(required=False,
            # label='y-axis',
            # choices=modeloutput.CHOICES)

    # choose_type = ChoiceField(required=False,
            # label='Graph type',
            # choices=(
                # ('scatter', 'scatter'),
                # ('pie', 'pie')
                # )
            # )


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


class Input(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = modelinput
        fields = calcfunc.__code__.co_varnames[:planner.__code__.co_argcount]

class Output(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = modeloutput
        fields = column(modeloutput.CHOICES)

class Graph(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Graph
        fields = ('graph_x', 'graph_y', 'graph_type')


