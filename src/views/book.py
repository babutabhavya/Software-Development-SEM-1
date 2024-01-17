from flask import Blueprint, jsonify, make_response, request

from models.book import Book, BookRequest
from utils.error_decorators import handle_exceptions

books_blueprint = Blueprint("books", __name__, url_prefix="/books")


@books_blueprint.route("/", methods=["GET"])
@handle_exceptions
def get_books():
    books = Book.list()
    print(books)
    return make_response(jsonify(books), 200)


@books_blueprint.route("/<int:book_id>", methods=["GET"])
@handle_exceptions
def get_book(book_id):
    book = Book.get(book_id)
    return make_response(jsonify(book), 200)


@books_blueprint.route("/", methods=["POST"])
@handle_exceptions
def add_book():
    data = request.get_json()
    book_request = BookRequest(**data)
    book: Book = Book.create(data=book_request)
    return make_response(jsonify(book), 201)


@books_blueprint.route("/<int:id>", methods=["PUT"])
@handle_exceptions
def update_book(id):
    data = request.get_json()
    book_request = BookRequest(**data)
    book = Book.update(data=book_request, id=id)
    return make_response(jsonify(book), 200)


@books_blueprint.route("/<int:id>", methods=["DELETE"])
@handle_exceptions
def delete_book(id):
    Book.delete(id=id)
    return make_response(jsonify({"message": "Book deleted successfully"}), 200)
