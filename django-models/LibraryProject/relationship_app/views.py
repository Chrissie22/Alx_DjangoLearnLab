from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages




# Create your views here.

def list_books(request): 
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.select_related('author').all()
        return context


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Registeration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
            
               
def home(request):
    return render(request, 'relationship_app/home.html')
            
        
    
