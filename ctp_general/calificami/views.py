from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request): 
    return render(request, 'calificami/index.html', {'title': 'Home'} )


def aboutus(request): 
    return render(request, 'calificami/about.html', {'title': 'Nosotros'} )

def login(request):
    return render(request, 'calificami/login.html', {'title': 'Entrar'} )

#def register(request):
#    return render(request, 'calificami/register.html', {'title': 'Registrate'} )

def privacy(request):
    return render(request, 'calificami/privacy.html', {'title': 'Privacidad'} )

def home(request): 
    context = {
        'posts' :  Post.objects.all()
    }
    return render(request, 'calificami/home.html', context )