from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *

def vizualisation(request):
    return render_to_response("lucyDJ/home.html",
            {"lines": Point.objects.all()})

# Create your views here.
