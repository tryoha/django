from django.urls import path

from .views import IndexView, DetailView, SearchResultsListView

app_name = 'crm'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<slug:slug>/', DetailView.as_view(), name='detail'),
]