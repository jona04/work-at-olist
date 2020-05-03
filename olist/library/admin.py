from django.contrib import admin

from olist.library.models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'edition', 'publication_year', 'created_at']
    search_fields = ['name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
