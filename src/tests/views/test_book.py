import json

import pytest

from app import app
from database import db

app.config["TESTING"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_database.sqlite.db"


@pytest.fixture
def test_app():
    with app.app_context():
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_database.sqlite.db"
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def sample_book_data():
    return {
        "title": "Sample Book",
        "author": "Sample Author",
        "published_date": "2022-01-01",
        "available_copies": 10,
    }


@pytest.fixture
def client(test_app):
    return test_app.test_client()


def test_get_books(client):
    response = client.get("/books/")
    assert response.status_code == 200
    assert json.loads(response.data) == []


def test_add_book(sample_book_data, client):
    response = client.post("/books/", json=sample_book_data)
    assert response.status_code == 201
    assert json.loads(response.data)["title"] == "Sample Book"


def test_get_book(test_app, sample_book_data):
    client = test_app.test_client()
    response = client.post("/books/", json=sample_book_data)
    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.get(f"/books/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["title"] == "Sample Book"


def test_update_book(client, sample_book_data):
    response = client.post("/books/", json=sample_book_data)

    updated_book_data = {
        "title": "Updated Sample Book",
        "author": "Updated Sample Author",
        "published_date": "2022-02-01",
        "available_copies": 15,
    }

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.put(f"/books/{id}", json=updated_book_data)
    assert response.status_code == 200
    assert json.loads(response.data)["title"] == "Updated Sample Book"


def test_delete_book(client, sample_book_data):
    response = client.post("/books/", json=sample_book_data)

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.delete(f"/books/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "Book deleted successfully"
