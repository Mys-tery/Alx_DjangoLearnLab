from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, delete for Author.
    The AuthorSerializer returns nested books (read-only) for each author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, delete for Book.
    BookSerializer validates publication_year and returns the author by id.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
