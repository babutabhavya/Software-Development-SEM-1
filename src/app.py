from flask import Flask

from views import *
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite.db"

from database import db


db.init_app(app)

migrate = Migrate(app, db)


def init_db():
    db_local = db
    db_local.init_app(app)
    migrate.init_app(app, db)


with app.app_context():
    db.create_all()


app.register_blueprint(health_blueprint)
app.register_blueprint(books_blueprint)
app.register_blueprint(libraries_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
