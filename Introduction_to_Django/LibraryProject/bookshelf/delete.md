
### 4. Delete Operation

**Command:**
```python
from bookshelf.models import Book
book.delete()
all_books = Book.objects.all()
print(all_books)


# Expected Output
# []
# (This confirms that the book has been deleted.)