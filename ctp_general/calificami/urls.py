from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ctd-index"),
    path('index/', views.index, name="ctd-index"),
    path('about/', views.aboutus, name="ctd-about"),
    path('login/', views.login, name='ctd-login'),
    path('privacy/', views.privacy, name="ctd-privacy"),
    #path('register/', views.register, name='ctd-register'),
    path('home/', views.home, name='ctd-home'),
    
]