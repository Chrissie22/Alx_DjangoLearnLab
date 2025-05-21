# Update the title
```python

from bookshelf.models import Book
book = Book.objects.get(title="Django")
book.title = "Django Models"
book.save()
print(book.title)
