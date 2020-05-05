from django.test import TestCase

from library.models import Author, Book, GroupBookAuthor
from olist.settings import INSTALLED_APPS


class EntryModelTest(TestCase):
    def test_string_representation_author(self):
        author = Author(name="Jonatas")
        self.assertEqual(str(author), author.name)

    def test_verbose_name_plural_author(self):
        self.assertEqual(str(Author._meta.verbose_name_plural), "Authors")

    def test_string_representation_book(self):
        book = Book(name="Book Jonatas")
        self.assertEqual(str(book), book.name)

    def test_string_representation_group_book(self):
        author = Author(name="Jonatas")
        book = Book(name="Book Jonatas")
        group = GroupBookAuthor(author=author, book=book)
        self.assertEqual(str(group), group.book.name)

    def test_verbose_name_plural_group_book(self):
        self.assertEqual(str(GroupBookAuthor._meta.verbose_name_plural), "Group Book Author s")
