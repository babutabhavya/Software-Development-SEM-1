from database import db
from pydantic import BaseModel
from .base import LibraryBaseModel


class UserRequest(BaseModel):
    email: str
    full_name: str


tags = db.Table(
    "user_libraries",
    db.Column("users_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column(
        "libraries_id", db.Integer, db.ForeignKey("libraries.id"), primary_key=True
    ),
)


class User(LibraryBaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)

    book = db.relationship("Book", backref="users", lazy=True)
