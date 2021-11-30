from django.shortcuts import render
from django.views import generic

# from .models import Client, ...

def index(request):
    return render(request, template_name='crm/index.html')