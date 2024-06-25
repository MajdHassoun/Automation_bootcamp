from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return self.books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

    def edit_book(self, old_title, new_book):
        for book in self.books:
            if book.title == old_title:
                book.title = new_book.title
                book.author = new_book.author
                book.year = new_book.year
                book.genre = new_book.genre
                return

    def to_dict(self):
        books_list = []
        for book in self.books:
            books_list.append(book.to_dict())
        return books_list

    @staticmethod
    def from_dict(data):
        library = Library()
        library.books = []
        for book_data in data:
            library.books.append(Book.from_dict(book_data))
        return library
