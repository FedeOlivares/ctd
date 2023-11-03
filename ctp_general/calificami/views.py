from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from .models import Post


def index(request): 
    return render(request, 'calificami/index.html', {'title': 'Home'} )


def aboutus(request): 
    return render(request, 'calificami/about.html', {'title': 'Nosotros'} )

def privacy(request):
    return render(request, 'calificami/privacy.html', {'title': 'Privacidad'} )

'''
def home(request): 
    context = {
        'posts' :  Post.objects.all()
    }
    return render(request, 'calificami/home.html', context )
'''

class PostListView(ListView):
    model = Post
    template_name = 'calificami/home.html'
    context_object_name = 'posts'
    ordering = ['-datePosted']
    
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'course']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'course']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False