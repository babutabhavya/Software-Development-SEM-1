from flask import jsonify, make_response
from pydantic import ValidationError


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except ValueError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    wrapper.__name__ = func.__name__
    return wrapper
