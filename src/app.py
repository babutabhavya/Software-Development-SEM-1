from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from views import health_blueprint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite.db"
db = SQLAlchemy(app)

app.register_blueprint(health_blueprint)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
