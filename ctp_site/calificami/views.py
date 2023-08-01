from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return HttpResponse('Welcome! to CTD')

def aboutus(request): 
    return HttpResponse('Welcome! to CTDs about us!')
