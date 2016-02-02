from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *

def vizualisation(request):
    return render_to_response("lucyDJ/home.html",
            {"lines": Point.objects.all()})

def accept_data(request):
    if request.method == 'GET':
        form = CalcParams(request.GET)
    else:
        form = CalcParams()
    return render(request, 'lucyDJ/home.html', {"form": form})

# Create your views here.
