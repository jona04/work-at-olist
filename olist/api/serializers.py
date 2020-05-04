from rest_framework import serializers

from olist.library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'created_at', 'uploaded_at')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors', 'created_at', 'uploaded_at')
