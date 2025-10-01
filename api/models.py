from django.db import models

class Author(models.Model):
    """
    Author Model:
    Stores author details.
    One Author can be linked to multiple Books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey 
    Author,
    related_name="books",   # enables Author.books access
    on_delete=models.CASCADE
