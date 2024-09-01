from rest_framework import serializers
from .models import Book  # Adjust the import if needed

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'