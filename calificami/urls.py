from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView,
)

urlpatterns = [
    path('', views.index, name="ctd-index"),
    path('index/', views.index, name="ctd-index"),
    path('about/', views.aboutus, name="ctd-about"),
    path('privacy/', views.privacy, name="ctd-privacy"),
    path('home/', PostListView.as_view(), name='ctd-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),    
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]