from django.contrib import admin

from olist.library.models import Book, Author, GroupBookAuthor


class GroupBookAuthorInline(admin.TabularInline):
    model = GroupBookAuthor
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'edition', 'publication_year', 'created_at']
    search_fields = ['name']

    inlines = (GroupBookAuthorInline,)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
