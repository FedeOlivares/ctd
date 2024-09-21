from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Repetí la contraseña'}))
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm (forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']