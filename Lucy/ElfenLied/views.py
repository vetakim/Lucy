from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from templatefilters import calcfilters
from .models import *
from .forms import *
from .digen import gendi
from numpy import random, sin, radians, cos
import sqlite3

def entry_db(funcreturn, modelname):
    '''Заполнение БД при помощи модели modelname списком словарей funcreturn'''
    for dictionary in funcreturn:
        modelname(**dictionary).save()
    return 0

def accept_data(request):
    parameters = { 'amplitude' : 1.0, 'samples' : 360 }
    toclear = False
    launch = False

    if request.method == 'GET':
        form = CalcParams(request.GET)

        if form.is_valid():
            parameters = form.cleaned_data
            toclear = parameters.pop('toclear')
            launch = parameters.pop('launch')
        else:
            print('FORM NOT VALID')
    else:
        form = CalcParams()

    if toclear:
        Point.objects.all().delete()
    elif launch:
        entry_db(gendi(**parameters), Point)

    return render(request, 'lucyDJ/home.html',
            {"form": form, "lines": Point.objects.values() })

# Create your views here.
