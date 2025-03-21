# Advanced API Project

## Overview
This project demonstrates the use of Django REST Framework to create an API with custom serializers and generic views.

## Endpoints
- `GET /api/books/`: List all books.
- **Filtering**: `/api/books/?title=SomeTitle`
- **Searching**: `/api/books/?search=SomeSearchTerm`
- **Ordering**: `/api/books/?ordering=publication_year`
- `POST /api/books/create/`: Create a new book (requires authentication).
- `GET /api/books/<int:pk>/`: Retrieve a single book by ID.
- `PUT /api/books/<int:pk>/update/`: Update an existing book (requires authentication).
- `DELETE /api/books/<int:pk>/delete/`: Delete a book (requires authentication).

## Permissions
- Unauthenticated users have read-only access to the API.
- Authenticated users can create, update, and delete books.

## Testing
Use tools like Postman or curl to test the API endpoints.

## Models
- **Author**: Represents an author with a name and age.
- **Book**: Represents a book with a title, publication year, and a foreign key to the Author model.

## Serializers
- **BookSerializer**: Serializes all fields of the Book model and includes custom validation for the publication year.
- **AuthorSerializer**: Serializes the name field and includes a nested BookSerializer to serialize related books dynamically.

## Views
- **BookListView**: Handles listing all books. Read-only access is allowed for unauthenticated users.
- **BookDetailView**: Handles retrieving a single book by ID. Read-only access is allowed for unauthenticated users.
- **BookCreateView**: Handles creating a new book. Requires authentication.
- **BookUpdateView**: Handles updating an existing book. Requires authentication.
- **BookDeleteView**: Handles deleting a book. Requires authentication.