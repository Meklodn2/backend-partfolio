from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name ='posts'
    ordering = ['-date_posted']



class PostDetailView(DetailView):
    model = Post
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'
