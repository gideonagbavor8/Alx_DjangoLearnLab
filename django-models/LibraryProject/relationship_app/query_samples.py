from relationship_app.models import Author, Book

from relationship_app.models import Author, Book

author_name = "Author Name"  
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)



from relationship_app.models import Library

from relationship_app.models import Library

library_name = "Library Name"  
library = Library.objects.get(name=library_name)
for book in library.books.all():
    print(book.title)



from relationship_app.models import Library, Librarian

library_name = "Library Name"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(librarian.name)

