from flask import Blueprint, jsonify, make_response, request

from models.book import Book, BookRequest
from utils.error_decorators import handle_exceptions

books_blueprint = Blueprint("books", __name__, url_prefix="/books")


@books_blueprint.route("/", methods=["GET"])
@handle_exceptions
def get_books():
    return make_response(jsonify(Book.list()), 200)


@books_blueprint.route("/<int:book_id>", methods=["GET"])
@handle_exceptions
def get_book(book_id):
    return make_response(jsonify(Book.get(book_id)), 200)


@books_blueprint.route("/", methods=["POST"])
@handle_exceptions
def add_book():
    data = request.get_json()
    book: Book = Book.create(data=BookRequest(**data))
    return make_response(jsonify(book), 201)


@books_blueprint.route("/<int:id>", methods=["PUT"])
@handle_exceptions
def update_book(id):
    data = request.get_json()
    book = Book.update(data=BookRequest(**data), id=id)
    return make_response(jsonify(book), 200)


@books_blueprint.route("/<int:id>", methods=["DELETE"])
@handle_exceptions
def delete_book(id):
    Book.delete(id=id)
    return make_response(jsonify({"message": "Book deleted successfully"}), 200)
