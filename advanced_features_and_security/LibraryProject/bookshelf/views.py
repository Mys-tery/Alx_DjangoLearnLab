# advanced_features_and_s/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('advanced_features_and_s.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

@permission_required('advanced_features_and_s.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect("book_list")
    return render(request, "add_book.html")

@permission_required('advanced_features_and_s.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect("book_list")
    return render(request, "edit_book.html", {"book": book})

@permission_required('advanced_features_and_s.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("book_list")
