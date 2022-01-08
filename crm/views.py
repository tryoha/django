from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Client


class IndexView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = "crm/index.html"
    login_url = 'account_login'
    permission_required = 'crm.special_status'


class DetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'
    template_name = "crm/detail.html"
    login_url = 'account_login'
    permission_required = 'crm.special_status'


class SearchResultsListView(ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = "crm/search_results.html"
    # queryset = Client.objects.filter(name__icontains='рога')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Client.objects.filter(
            Q(name__icontains=query) | Q(adress__icontains=query)
        )
