from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
]
