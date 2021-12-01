from django.shortcuts import render
from django.utils.translation import templatize
from django.views import generic

from .models import Client


class IndexView(generic.ListView):
    model = Client
    template_name = "crm/index.html"


class DetailView(generic.DetailView):
    model = Client
    template_name = "crm/detail.html"
