from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *
from .digen import gendi
from numpy import random, sin, radians, cos
import sqlite3
import sys
from priority.scheduler import planner

import sys
from django.http import HttpResponse

def print_http_response(f):
    """ Wraps a python function that prints to the console, and returns
    those results as a HttpResponse (HTML)"""

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content])
    return new_f

def entry_db(funcreturn, modelname):
    '''Заполнение БД при помощи модели modelname списком словарей funcreturn'''
    for dictionary in funcreturn:
        modelname(**dictionary).save()
    return 0

func = planner
modelname = RequisitionOutput
paramform = Input
outform = Output

# @print_http_response
def accept_data(request):

    parameters = dict(zip(
                func.__code__.co_varnames, func.__defaults__
                ))

    calcfuncname = func.__name__
    toclear = False
    launch = False
    graph_x = modelname.CHOICES[0][0]
    graph_y = modelname.CHOICES[1][0]
    category = modelname.CHOICES[1][0]
    graph_type = 'scatter'
    calcout = {}
    lines = modelname.objects.values()

    if request.method == 'GET':
        cform = CalcClear(request.GET)
        gform = Graph(request.GET)
        oform = outform(request.GET)
        form = paramform(request.GET)

        if form.is_valid():
            parameters = form.cleaned_data
        else:
            print('PARAMETERS FORM NOT VALID:\n%s' % form.errors)

        if gform.is_valid():
            graph_x = gform.cleaned_data['graph_x']
            graph_y = gform.cleaned_data['graph_y']
            category = gform.cleaned_data['category']
            graph_type = gform.cleaned_data['graph_type']
        else:
            print('GRAPH FORM NOT VALID')

        if cform.is_valid():
            toclear = cform.cleaned_data['toclear']
            launch = cform.cleaned_data['launch']
        else:
            print('MANAGEMENT FORM NOT VALID')

        if oform.is_valid():
            calcout = oform.cleaned_data
        else:
            print('OUTPUT FORM NOT VALID')
    else:
        form = paramform()
        cform = CalcClear()
        oform = outform()
        gform = Graph()
    print(calcout)

    if launch:
        modelname.objects.all().delete()
        entry_db(func(**parameters), modelname)
        lines = modelname.objects.values()
        # xylines = lines.filter(category
        cform = CalcClear()

    if toclear:
        modelname.objects.all().delete()

    # lines = lines.filter(distance=1)
    return render(request, 'lucyDJ/home.html',
            {"form": form,
             "funcname": calcfuncname,
             "cform": cform,
             "oform": oform,
             "gform": gform,
             "calcout": calcout,
             "graph_y": graph_y,
             "graph_x": graph_x,
             "category": category,
             "graph_type": graph_type,
             "lines": lines})

# Create your views here.

