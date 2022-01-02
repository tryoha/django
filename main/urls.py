from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('signup/', views.SignupPageView.as_view(), name='signup'),   
    path("signin/", views.signin, name="signin"),
    path('', views.index, name='index'),

]