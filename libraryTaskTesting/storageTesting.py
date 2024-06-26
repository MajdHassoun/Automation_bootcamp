import json
import os
import tempfile
import unittest
from storage import save_library, load_library, FILE_PATH
from book import Book
from library import Library


class TestStorage(unittest.TestCase):
    def test_save_library(self):
        # Arrange
        book1 = Book("hello", "its me", "2002", "music")
        book2 = Book("hell", "its", "20", "mu")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)
        save_library(library)

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_filename = temp_file.name
        temp_file.close()

        # Act
        library.filename = temp_filename  # Use the temporary file for saving
        save_library(library, temp_filename)

        # Assert
        with open(temp_filename, 'r') as file:
            data = json.load(file)
            expected_data = library.to_dict()
            self.assertEqual(data, expected_data, "The saved library data does not match the expected data")

        # Clean up
        os.remove(temp_filename)

    def test_load_library(self):
        book1 = Book("hello", "its me", "2002", "music")
        book2 = Book("hell", "its", "20", "mu")
        library = Library()
        library.add_book(book1)
        library.add_book(book2)
        save_library(library)

        expected_list = [
            {'title': 'hello', 'author': 'its me', 'year': '2002', 'genre': 'music'},
            {'title': 'hell', 'author': 'its', 'year': '20', 'genre': 'mu'}
        ]

        actual_library = load_library()

        # Get the actual list of books from the loaded library
        actual_list = []
        for book in actual_library.list_books():
            actual_list.append(book.to_dict())

        self.assertEqual(expected_list, actual_list)
