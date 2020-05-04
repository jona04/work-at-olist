from rest_framework import serializers

from olist.library.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'author', 'created_at', 'uploaded_at')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'created_at', 'uploaded_at')
