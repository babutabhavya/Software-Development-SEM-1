from flask import Flask

from database import db
from views import books_blueprint, health_blueprint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite.db"

db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(health_blueprint)
app.register_blueprint(books_blueprint)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
