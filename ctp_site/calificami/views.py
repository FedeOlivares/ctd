from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return render(request, 'calificami/index.html')


def aboutus(request): 
    return render(request, 'calificami/about.html')

def login(request):
    return render(request, 'calificami/login.html')

def privacy(request):
    return render(request, 'calificami/privacy.html')