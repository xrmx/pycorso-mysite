from django.contrib import admin
from .models import Book, Author, BookInstance, Genre


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
