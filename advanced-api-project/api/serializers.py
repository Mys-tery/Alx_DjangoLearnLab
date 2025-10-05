from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book instances.
    Fields:
      - id: auto id
      - title
      - publication_year
      - author: by default this is represented by the author's pk (id)
    Validation:
      - publication_year is validated to ensure it is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom field-level validation for publication_year.
        Prevents setting a publication year greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author instances and includes a nested list of books.
    - name: the author's name
    - books: a nested list of BookSerializer objects for all books related to the author.
      The nested books are read-only here. They are dynamically pulled from Book.objects.filter(author=this_author)
      thanks to Book.author having related_name='books'.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
