from django import forms
from .models import Book

# Example: Search form for books
class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )

# Example: Model form for Book (optional, if you want add/edit functionality)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
