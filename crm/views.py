from django.shortcuts import render
from django.utils.translation import templatize
from django.views import generic

from .models import Client


class IndexView(generic.ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = "crm/index.html"


class DetailView(generic.DetailView):
    model = Client
    context_object_name = 'client'
    template_name = "crm/detail.html"
