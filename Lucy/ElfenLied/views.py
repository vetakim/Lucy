from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *
from .digen import gendi
from numpy import random, sin, radians, cos
import sqlite3
import sys
from priority.scheduler import planner

def entry_db(funcreturn, modelname):
    '''Заполнение БД при помощи модели modelname списком словарей funcreturn'''
    for dictionary in funcreturn:
        modelname(**dictionary).save()
    return 0

func = planner
modelname = Requisitions
paramform = ReqParams

def accept_data(request):
    parameters = dict.fromkeys(
            func.__code__.co_varnames[
                :func.__code__.co_argcount])
    print(parameters)
    toclear = False
    launch = False
    graph_y = modelname.CHOICES[0]
    graph_x = modelname.CHOICES[1]

    if request.method == 'GET':
        cform = CalcClear(request.GET)
        form = paramform(request.GET)

        if form.is_valid():
            parameters = form.cleaned_data
        else:
            print('FORM NOT VALID')

        if cform.is_valid():
            toclear = cform.cleaned_data['toclear']
            launch = cform.cleaned_data['launch']
            graph_x = cform.cleaned_data['choose_x_points']
            graph_y = cform.cleaned_data['choose_y_points']
        else:
            print('CFORM NOT VALID')
    else:
        form = paramform()
        cform = CalcClear()

    if launch:
        modelname.objects.all().delete()
        entry_db(func(**parameters), modelname)
        # form = paramform(parameters)
        cform = CalcClear()

    if toclear:
        modelname.objects.all().delete()

    return render(request, 'lucyDJ/home.html',
            {"form": form,
             "cform": cform,
             "graph_y": graph_y,
             "graph_x": graph_x,
             "lines": modelname.objects.values()})

# Create your views here.

