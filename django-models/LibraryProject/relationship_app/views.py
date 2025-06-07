from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Librarian
from .models import Library
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView



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
        context['books'] = self.objects.books.select_related('author').all()
        return context
    
def home(request):
    return render(request, 'relationship_app/home.html')
            
        
    
