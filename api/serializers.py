# api/serializers.py
from rest_framework import serializers
import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book objects. It exposes all model fields.

    Validation:
    - `validate_publication_year` ensures the year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not greater than the current year.
        This method is called automatically by DRF when validating the serializer.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author objects and includes a nested representation of related books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
