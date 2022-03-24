from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from . models import Post
from django.views.generic.edit import CreateView
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = 'author','title','content'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = 'title','content'