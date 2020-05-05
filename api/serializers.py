from rest_framework import serializers

from library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'created_at', 'uploaded_at')


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)
    # authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    authors = AuthorSerializer(read_only=True, many=True)
    authors_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'edition', 'publication_year', 'authors', 'authors_id', 'created_at', 'uploaded_at')
        read_only_fields = ('pk', 'created_at', 'updated_at')

    # def get_validation_exclusions(self, *args, **kwargs):
    #     exclusions = super(BookSerializer, self).get_validation_exclusions()
    #
    #     return exclusions + ['author']

    def create(self, validated_data):
        authors = validated_data.pop('authors_id')
        book = Book.objects.create(**validated_data)
        for author in authors:
            book.authors.add(author)
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors_id')
        book = Book.objects.create(**validated_data)
        for author in authors:
            book.authors.add(author)
        return book
