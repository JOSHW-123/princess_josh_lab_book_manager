from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import author_repository, book_repository

books_blueprint = Blueprint("books", __name__)

# NEW
# GET '/books/new'
@books_blueprint.route("/book/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("book/new.html", all_authors=authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    author_id = request.form["author_id"]
    author = author_repository.select(author_id)
    new_book = Book(book_title, genre, publisher, author)
    book_repository.save(new_book)
    return redirect("/books")


# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
