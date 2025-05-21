# Deleting a Book Record

To delete a book record using Django’s ORM, first import the `Book` model:

```python
from bookshelf.models import Book


book = Book.objects.get(id=1)
book.delete()

