from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import *

# Create your views here.
# creating the class based views
# creating the class based view PostListView to inherit the ListView Generic class behavior
# NOTE: Template_name or context_object_name were not indicated in all class based views, in essense, the views uses
# default template name and context_object_name to render the information nicely.

class PostListView(ListView):
    model = Post
    
# creating the class based view PostCreateView to inherit the CreateView Generic class behavior
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
  
# creating the class based view PostDetailView to inherit the DetailView Generic class behavior
class PostDetailView(DetailView):
    model = Post
    
# creating the class based view PostUpdateView to inherit the UpdateView Generic class behavior
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
# creating the class based view PostDeleteView to inherit the DeleteView Generic class behavior
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:all")
