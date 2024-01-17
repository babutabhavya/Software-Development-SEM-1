from flask import Blueprint, Response, make_response

health_blueprint = Blueprint("health", __name__, url_prefix="/health")


@health_blueprint.route("/", methods=["GET"])
def health():
    return Response(make_response({"message": "Success"}), status=200)
