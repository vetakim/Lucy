from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *
from numpy import random, sin, radians
import sqlite3

def accept_data(request):
    amplitude = 1.0
    toclear = False
    if request.method == 'GET':
        form = CalcParams(request.GET)
        if form.is_valid():
            amplitude = form.cleaned_data['amplitude']
            toclear = form.cleaned_data['toclear']
        else:
            print('FORM NOT VALID')
    else:
        form = CalcParams()

    if not toclear:
        for j in range(0, 360, 1):
            print('\r%s' % j, end='')
            Point(abscissa=j, ordinate=amplitude *
                    sin(radians(j)))
    else:
        Point.objects.all().delete()

    return render(request, 'lucyDJ/home.html',
            {"form": form,
                "lines": Point.objects.all(),
                "amplitude": amplitude})

# Create your views here.
