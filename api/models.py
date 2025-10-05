# api/models.py
from django.db import models


class Author(models.Model):
    """
    Author model: represents an author.

    Fields:
    - name: stores the author's name as a string.

    Relationship:
    - An Author can have many Book objects (one-to-many).
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: represents a book written by an Author.

    Fields:
    - title: book title.
    - publication_year: integer year when the book was published.
    - author: foreign key to Author establishing the one-to-many relation.

    Note on `related_name`: we set `related_name='books'` so we can do
        author.books.all()
    to get the Author's books. This also makes serialization clearer.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
