from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('<slug:category_slug>/<slug:slug>/', views.NewsView.as_view(), name='detail')
]