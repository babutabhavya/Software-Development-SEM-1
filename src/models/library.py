from typing import List

from pydantic import BaseModel

from models.book import Book
from models.user import User


class Library(BaseModel):
    books: List[Book]
    users: List[User]
