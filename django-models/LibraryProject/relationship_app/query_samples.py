from relationship_app.models import Author, Book

author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)


from relationship_app.models import Library

library = Library.objects.get(name="Library Name")
for book in library.books.all():
    print(book.title)


from relationship_app.models import Library, Librarian

library = Library.objects.get(name="Library Name")
librarian = Librarian.objects.get(library=library)
print(librarian.name)
