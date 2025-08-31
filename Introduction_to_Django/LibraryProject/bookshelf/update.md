# Update a Book

from bookshelf.models import Book

book = Book.objects.get(title='1984')
book.publication_year = 1950
book.save()

