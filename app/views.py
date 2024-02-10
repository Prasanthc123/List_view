from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from app.models import *

class Schoollist(ListView):
    model=School
    ordering=['sname']
    context_object_name='schools'