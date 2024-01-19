from typing import Optional

from pydantic import BaseModel

from database import db

from .base import LibraryBaseModel
from .library import Library


class BookRequest(BaseModel):
    title: str
    author: str
    published_date: str
    library_id: int


class Book(LibraryBaseModel):
    __tablename__ = "books"

    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.String(20), nullable=False)

    library_id = db.Column(db.Integer, db.ForeignKey("libraries.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @classmethod
    def create(cls, data: BaseModel):
        library_id = data.library_id
        print("Data here", data)

        existing_library = Library.get(library_id)

        if not existing_library:
            raise ValueError(f"Library with id {library_id} does not exist.")

        return super(Book, cls).create(data)
