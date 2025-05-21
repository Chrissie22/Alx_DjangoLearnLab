## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="Django", author="George Orwell", publication_year=1949)
book  # Output: <Book: 1984 by George Orwell (1949)>


## Update

from bookshelf .models import Book
book = Book.objects.get(title="Django")
book.title = "Django Models"
book.save()
print(book.title)


## Delete

from bookshelf .models import Book
book = Book.objects.get(title="Django Models")
book.delete()
book.objects.all()

##Update 

from bookshelf.models import Book
book = Book.objects.get(title="Django")
book.title = "Django Models"
book.save()
print(book.title)



