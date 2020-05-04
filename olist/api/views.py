from rest_framework import viewsets, filters

from olist.api.serializers import BookSerializer, AuthorSerializer
from olist.library.models import Book, Author


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = 'name'


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = 'name'
