import unittest
from library import Library
# from libraryTaskTesting.app import add_book
from libraryTaskTesting.book import Book


class TestLibrary(unittest.TestCase):

    def test_library_init(self):
        library = Library()
        self.assertListEqual(library.books, [])

    def test_add_book_true(self):
        # Arrange
        library = Library()
        book1 = Book("hello", "its me", "2002", "music")

        # Act
        library.add_book(book1)

        # Assert

        self.assertIn(book1, library.books)

    def test_find_book_true(self):
        library = Library()
        book1 = Book("hello", "its me", "2002", "music")
        library.add_book(book1)
        book2 = library.find_book(book1.title)

        self.assertEquals(book2, book1)

    def test_delete_book(self):
        library = Library()
        book1 = Book("hello", "its me", "2002", "music")
        library.add_book(book1)
        library.delete_book(book1)
        self.assertIsNot(library.books, book1)

    def test_edit_book(self):
        library = Library()
        book1 = Book("hello", "its me", "2002", "music")
        library.add_book(book1)
        book2 = Book("hell", "its", "20", "mu")
        library.edit_book("hello", book2)
        self.assertEqual(book2.title, "hell")
        self.assertEqual(book2.author, "its")
        self.assertEqual(book2.year, "20")
        self.assertEqual(book2.genre, "mu")

    def test_to_dict_library(self):
        book1 = Book("hello", "its me", "2002", "music")
        book2 = Book("hell", "its", "20", "mu")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)
        list_books = \
            [{'title': 'hello', 'author': 'its me', 'year': '2002', 'genre': 'music'},
             {'title': 'hell', 'author': 'its', 'year': '20', 'genre': 'mu'}]

        lst_dict = library.to_dict()
        self.assertListEqual(list_books, lst_dict)

    def test_from_dict(self):
        data = [
            {'title': 'hello', 'author': 'its me', 'year': '2002', 'genre': 'music'},
            {'title': 'hell', 'author': 'its', 'year': '20', 'genre': 'mu'}
        ]

        library = Library.from_dict(data)

        self.assertEqual(len(library.books), 2)

        self.assertEqual(library.books[0].title, 'hello')
        self.assertEqual(library.books[0].author, 'its me')
        self.assertEqual(library.books[0].year, '2002')
        self.assertEqual(library.books[0].genre, 'music')

        self.assertEqual(library.books[1].title, 'hell')
        self.assertEqual(library.books[1].author, 'its')
        self.assertEqual(library.books[1].year, '20')
        self.assertEqual(library.books[1].genre, 'mu')
