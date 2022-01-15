from django.shortcuts import render
from django.views import generic

from .models import Category, Product

# Create your views here.

class IndexView(generic.ListView):
    pass