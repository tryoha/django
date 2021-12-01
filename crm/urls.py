from django.urls import path

from . import views

app_name = 'crm'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
]