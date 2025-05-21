# Create a Book instance
from bookshelf.models import Book
book = Book.objects.create(title="Django", author="Chrissie George", publication_year=1949)
book
