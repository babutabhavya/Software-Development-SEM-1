from flask import Blueprint, jsonify, make_response, request
from models.user import User, UserRequest
from utils.error_decorators import handle_exceptions

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.route("/", methods=["GET"])
@handle_exceptions
def get_users():
    return make_response(jsonify(User.list()), 200)


@users_blueprint.route("/<int:user_id>", methods=["GET"])
@handle_exceptions
def get_user(user_id):
    return make_response(jsonify(User.get(user_id)), 200)


@users_blueprint.route("/", methods=["POST"])
@handle_exceptions
def add_user():
    data = request.get_json()
    user: User = User.create(data=UserRequest(**data))
    return make_response(jsonify(user), 201)


@users_blueprint.route("/<int:id>", methods=["PUT"])
@handle_exceptions
def update_user(id):
    data = request.get_json()
    user = User.update(data=UserRequest(**data), id=id)
    return make_response(jsonify(user), 200)


@users_blueprint.route("/<int:id>", methods=["DELETE"])
@handle_exceptions
def delete_user(id):
    User.delete(id=id)
    return make_response(jsonify({"message": "User deleted successfully"}), 200)
