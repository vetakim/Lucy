from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *
from .digen import gendi
from numpy import random, sin, radians, cos
import sqlite3

def accept_data(request):
    amplitude = 1.0
    toclear = True
    samples = 360

    if request.method == 'GET':
        form = CalcParams(request.GET)
        if form.is_valid():
            amplitude = form.cleaned_data['amplitude']
            toclear = form.cleaned_data['toclear']
            samples = form.cleaned_data['samples']
        else:
            print('FORM NOT VALID')
    else:
        form = CalcParams()

    if not toclear:
        for j in gendi(amplitude, samples):
            Point(abscissa = j['abscissa'],
                    ordinate = j['ordinate'],
                    noise = j['noise']
                    ).save()
    else:
        Point.objects.all().delete()

    return render(request, 'lucyDJ/home.html',
            {"form": form,
                "lines": Point.objects.values(),
                "amplitude": amplitude})

# Create your views here.
