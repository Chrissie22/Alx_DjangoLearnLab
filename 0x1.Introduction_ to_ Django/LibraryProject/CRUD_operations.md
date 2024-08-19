```python
<!-- Opening a Django shell -->
python3 manage.py shell

<!-- Confirmimg the Book class -->
from bookshelf.models import Book

Book
<class 'bookshelf.models.Book'>

Book.objects.all()
<QuerySet []>

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

<!-- Expected output -->
<Book: 1984 is written by George Orwell >

<!-- Retrieve the book -->

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

<!-- Expected output -->
The book tittle is 1984, author is George Orwell, published year is 1949

<!-- Update the titlle of the book-->
book.title = "Nineteen Eighty-Four"
book.save()

<!-- Expected Output -->
<Book: Nineteen Eighty-Four by George Orwell>

<!-- Delete Operation -->
book.delete()
books = Book.objects.all()
print(books) #to confirm the deletion

<!-- Expected output -->
<QuerySet []>
