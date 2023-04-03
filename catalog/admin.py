from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# Register your models here.


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
