from typing import Optional

from pydantic import BaseModel

from database import db

from .base import LibraryBaseModel


class BookRequest(BaseModel):
    title: str
    author: str
    published_date: str
    available_copies: Optional[int] = 200


class Book(LibraryBaseModel):
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.String(20), nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
