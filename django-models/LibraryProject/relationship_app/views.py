from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.all()
    response_html = "<h1>Books Available:</h1><ul>"
    for book in books:
        response_html += f"<li>{book.title} by {book.author.name}</li>"
    response_html += "</ul>"
    return HttpResponse(response_html)


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
