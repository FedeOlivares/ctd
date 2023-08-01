from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    context = { 'title' : 'Index',
    }
    return render(request, 'calificami/index.html', context)

def aboutus(request): 
    return HttpResponse('Welcome! to CTDs about us!')
