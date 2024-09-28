from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView
    )
from .models import Post


def index(request): 
    is_mobile = request.user_agent.is_mobile
    return render(request, 'calificami/index.html', {'title': 'Home'}, 
                   {'is_mobile': is_mobile})


def aboutus(request): 
    is_mobile = request.user_agent.is_mobile
    return render(request, 'calificami/about.html', {'title': 'Nosotros'},
                   {'is_mobile': is_mobile} )

def privacy(request):
    is_mobile = request.user_agent.is_mobile
    return render(request, 'calificami/privacy.html', {'title': 'Privacidad'}, 
                   {'is_mobile': is_mobile} )


class PostListView(ListView):
    model = Post
    template_name = 'calificami/home.html'
    context_object_name = 'posts'
    ordering = ['-datePosted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'calificami/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-datePosted')
    
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'course']
    success_url = '/home/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'course']
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False