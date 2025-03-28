from django.db import models

# The Author model represents an author with a name.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)

    def __str__(self):
        return self.name

# The Book model represents a book with a title, publication year, and a foreign key to the Author model.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title