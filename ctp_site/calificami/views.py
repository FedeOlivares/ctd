from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return render(request, 'calificami/index.html')


def aboutus(request): 
    return HttpResponse('Welcome! to CTDs about us!')