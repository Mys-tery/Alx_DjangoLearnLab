from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering
    filterset_fields = ['publication_year', 'author__name']

    # Searching
    search_fields = ['title', 'author__name']

    # Ordering
    ordering_fields = ['publication_year', 'title']
    ordering = ['publication_year']  # Default order
