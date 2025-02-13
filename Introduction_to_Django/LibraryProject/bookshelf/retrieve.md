
### 2. Retrieve Operation

**Command:**
```python
all_books = Book.objects.all()
for b in all_books:
    print(b.title, b.author, b.publication_year)


# Expected Output
# 1984 George Orwell 1949

