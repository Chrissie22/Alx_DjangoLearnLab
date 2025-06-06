from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Librarian, Library
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.

def list_books(request): 
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"
    
