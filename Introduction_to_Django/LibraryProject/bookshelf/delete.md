```python

book = Book.objects.get(title="Django Models")
book.delete()
Book.objects.all()
