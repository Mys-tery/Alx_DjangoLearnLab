from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="Chimamanda Ngozi Adichie")
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author1)
        self.book2 = Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author=self.author2)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-create')
        data = {"title": "Purple Hibiscus", "publication_year": 2003, "author": self.author2.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="Purple Hibiscus").author, self.author2)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "Purple Hibiscus", "publication_year": 2003, "author": self.author2.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Things Fall Apart Updated"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart Updated")

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Unauthorized Update"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_books(self):
        url = reverse('book-list') + "?search=Half"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Half of a Yellow Sun")

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f"?author={self.author1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list') + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2006)
        self.assertEqual(response.data[1]['publication_year'], 1958)
