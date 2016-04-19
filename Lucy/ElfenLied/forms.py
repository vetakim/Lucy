from django.forms import *
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import *

from priority.scheduler import planner
from priority.sharetools import column
from priority.shed import laws

modeloutput = RequisitionOutput
modelinput = RequisitionInput
calcfunc = planner

class CalcClear(forms.Form):

    launch = BooleanField(required=False, label='Calculate')

    toclear = BooleanField(required=False, label='',
            widget=forms.TextInput(attrs={
                'type': 'submit', 'value': 'Clear DB' }))

class Input(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    class Meta:
        model = modelinput
        fields = calcfunc.__code__.co_varnames[:calcfunc.__code__.co_argcount]
        labels = {j: _(j.capitalize(),) for j in fields}

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
        fields = ('graph_x', 'graph_y', 'category', 'graph_type')

