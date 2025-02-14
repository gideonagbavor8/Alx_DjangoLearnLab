# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('author', 'publication_year')  # Fields to filter by
    search_fields = ('title', 'author')  # Fields to search by
