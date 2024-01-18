from pydantic import BaseModel

from database import db

from .base import LibraryBaseModel


class LibraryRequest(BaseModel):
    name: str


class Library(LibraryBaseModel):
    __tablename__ = "libraries"

    name = db.Column(db.String(100), nullable=False)

    books = db.relationship("Book", back_populates="library")
