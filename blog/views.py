from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from . models import Post
from django.views.generic.edit import CreateView, DeleteView
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = 'author','title','content'
    success_message = "%(field)s - criado com sucesso"
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

class BlogUpdateView(SuccessMessageMixin,UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = 'title','content'
    success_message = "%(field)s - alterado com sucesso"
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )

class BlogDeleteView(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "%(field)s - deletado com sucesso"
    
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )