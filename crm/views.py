from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from .models import Client


class IndexView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = "crm/index.html"
    login_url = 'account_login'
    permission_required = 'crm.special_status'


class DetailView(PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = Client
    context_object_name = 'client'
    template_name = "crm/detail.html"
    login_url = 'account_login'
    permission_required = 'crm.special_status'
