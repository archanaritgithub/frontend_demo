from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

