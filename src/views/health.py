from flask import Blueprint

from models.response import ResponseModel

health_blueprint = Blueprint("health", __name__, url_prefix="/health")


@health_blueprint.route("/", methods=["GET"])
def health():
    return ResponseModel(message="Success", status_code=200).model_dump()
