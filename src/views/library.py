from flask import Blueprint, jsonify, make_response, request

from models.library import Library, LibraryRequest
from utils.error_decorators import handle_exceptions

libraries_blueprint = Blueprint("libraries", __name__, url_prefix="/libraries")


@libraries_blueprint.route("/", methods=["GET"])
@handle_exceptions
def get_libraries():
    return make_response(jsonify(Library.list()), 200)


@libraries_blueprint.route("/<int:library_id>", methods=["GET"])
@handle_exceptions
def get_library(library_id):
    return make_response(jsonify(Library.get(library_id)), 200)


@libraries_blueprint.route("/", methods=["POST"])
@handle_exceptions
def add_library():
    data = request.get_json()
    library: Library = Library.create(data=LibraryRequest(**data))
    return make_response(jsonify(library), 201)


@libraries_blueprint.route("/<int:id>", methods=["PUT"])
@handle_exceptions
def update_library(id):
    data = request.get_json()
    library = Library.update(data=LibraryRequest(**data), id=id)
    return make_response(jsonify(library), 200)


@libraries_blueprint.route("/<int:id>", methods=["DELETE"])
@handle_exceptions
def delete_library(id):
    Library.delete(id=id)
    return make_response(jsonify({"message": "Library deleted successfully"}), 200)
