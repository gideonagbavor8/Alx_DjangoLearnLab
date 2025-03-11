# advanced_api_project/api/serializers.py

from rest_framework import serializers
from .models import Author, Book
import datetime

# The BookSerializer serializes all fields of the Book model and includes custom validation for the publication year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer serializes the name field and includes a nested BookSerializer to serialize related books dynamically.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']