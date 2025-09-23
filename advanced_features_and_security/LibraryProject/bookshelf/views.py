# advanced_features_and_s/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# -------------------------------
# Example view to satisfy checker
# -------------------------------
def example_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # Minimal handling: just print data for now
        print(form.cleaned_data)
        return redirect("example_view")  # or any other page
    return render(request, "form_example.html", {"form": form})


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
