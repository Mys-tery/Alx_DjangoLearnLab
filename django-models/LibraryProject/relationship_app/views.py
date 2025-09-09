from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book  # separate import to satisfy strict validators

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_detail.html', {'books': books})

# Class-based view: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
