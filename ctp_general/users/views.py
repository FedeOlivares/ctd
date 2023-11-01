from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registrame(request):
    form = UserCreationForm()
    return render(request, 'users/registrame.html', {'form':form})