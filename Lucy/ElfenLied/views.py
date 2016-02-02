from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import *

def accept_data(request):
    amplitude = 1.0
    if request.method == 'GET':
        form = CalcParams(request.GET)
        if form.is_valid():
            amplitude = form.cleaned_data['amplitude']
        else:
            print('FORM NOT VALID')
    else:
        form = CalcParams()
    return render(request, 'lucyDJ/home.html',
            {"form": form,
                "lines": Point.objects.all(),
                "amplitude": amplitude})

# Create your views here.
