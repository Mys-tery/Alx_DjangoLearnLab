# Advanced API Project — Django REST Framework

Build an advanced API using **Django REST Framework (DRF)** that demonstrates:

- Custom models and serializers with nested relationships.
- Custom views and generic class-based views for CRUD operations.
- Proper use of permissions and validation.
  API Endpoints

| Method    | Endpoint         | Description              | Auth Required |
| --------- | ---------------- | ------------------------ | ------------- |
| GET       | /api/books/      | List all books           | No            |
| POST      | /api/books/      | Create a new book        | Yes           |
| GET       | /api/books/<id>/ | Retrieve a specific book | No            |
| PUT/PATCH | /api/books/<id>/ | Update a specific book   | Yes           |
| DELETE    | /api/books/<id>/ | Delete a specific book   | Yes           |
