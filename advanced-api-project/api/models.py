from django.db import models

class Author(models.Model):
    """
    Author model: stores author metadata.
    Fields:
      - name: The author's full name (string).
    Relationship:
      - An Author can have many Book instances (one-to-many).
      The reverse relation is available as `author.books` because Book uses related_name='books'.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: stores book information linked to an Author.
    Fields:
      - title: Title of the book (string).
      - publication_year: The year the book was published (integer).
      - author: ForeignKey to Author to model a many-to-one relationship (many books -> one author).
        The related_name 'books' allows accessing an author's books via `author.books.all()`.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
