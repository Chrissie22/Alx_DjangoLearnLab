from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

@login_required

def profile(request):
    return render(request, 'profile.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})