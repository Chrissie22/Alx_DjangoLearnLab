from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def login_view(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')