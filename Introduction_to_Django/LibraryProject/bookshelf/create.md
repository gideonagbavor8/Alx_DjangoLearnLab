# Create Operation

## Command
```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output
# Book instance "1984" created successfully.
