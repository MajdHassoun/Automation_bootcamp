import unittest
from book import Book


class TestBook(unittest.TestCase):
    def test_book_init(self):
        book = Book("majd's life", "majdH", "2022", "action")
        self.assertEqual(book.title, "majd's life")
        self.assertEqual(book.author, "majdH")
        self.assertEqual(book.year, "2022")
        self.assertEqual(book.genre, "action")

    def test_to_dict_book(self):
        book1 = Book("hello", "its me", "2002", "music")
        dic1 = book1.to_dict()
        dic2 = {'title': 'hello', 'author': 'its me', 'year': '2002', 'genre': 'music'}
        self.assertEqual(dic1, dic2)

    def test_from_dict_book(self):
        data = {'title': 'hello', 'author': 'its me', 'year': '2002', 'genre': 'music'}
        book1 = Book("hello", "its me", "2002", "music")
        book2 = Book.from_dict(data)
        self.assertEqual(book1.title, book2.title)
        self.assertEqual(book1.author, book2.author)
        self.assertEqual(book1.year, book2.year)
        self.assertEqual(book1.genre, book2.genre)
