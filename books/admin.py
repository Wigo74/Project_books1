from django.contrib import admin

from books.models import Author, Books, Readers


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "name", "photo", "created", "updated")
    list_display_links = ["name", "last_name"]
    search_fields = ["name", "last_name"]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "number_of_pages", "author", "books", "created", "updated")
    list_display_links = ["title", "author"]


@admin.register(Readers)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "last_name", "phone", "books", 'is_active')
    list_display_links = ["books"]
