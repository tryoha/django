from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='main/index.html')

def signin(request):
    return render(request, 'main/signin.html')