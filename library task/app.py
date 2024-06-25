from flask import Flask, render_template, request, redirect, url_for
from book import Book

from storage import save_library, load_library

app = Flask(__name__)
library = load_library()

@app.route('/')
def index():
    books = library.list_books()
    return render_template('list_books.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        book = Book(title, author, year, genre)
        library.add_book(book)
        save_library(library)
        return redirect(url_for('index'))
    return render_template('add_book.html')


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    book = library.find_book(title)
    if request.method == 'POST':
        new_title = request.form['title']
        new_author = request.form['author']
        new_year = request.form['year']
        new_genre = request.form['genre']
        new_book = Book(new_title, new_author, new_year, new_genre)
        library.edit_book(title, new_book)
        save_library(library)
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)


@app.route('/delete/<title>', methods=['GET', 'POST'])
def delete_book(title):
    if request.method == 'POST':
        library.delete_book(title)
        save_library(library)
        return redirect(url_for('index'))
    book = library.find_book(title)
    return render_template('delete_book.html', book=book)


if __name__ == '__main__':
    app.run(debug=True)
