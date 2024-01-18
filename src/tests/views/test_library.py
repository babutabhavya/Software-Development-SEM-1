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
def sample_library_data():
    return {
        "name": "Sample Library",
    }


@pytest.fixture
def client(test_app):
    return test_app.test_client()


def test_get_libraries(client):
    response = client.get("/libraries/")
    print(response.data)
    assert response.status_code == 200
    assert json.loads(response.data) == []


def test_add_library(sample_library_data, client):
    response = client.post("/libraries/", json=sample_library_data)
    assert response.status_code == 201
    assert json.loads(response.data)["name"] == "Sample Library"


def test_get_library(test_app, sample_library_data):
    client = test_app.test_client()
    response = client.post("/libraries/", json=sample_library_data)
    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.get(f"/libraries/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["name"] == "Sample Library"


def test_update_library(client, sample_library_data):
    response = client.post("/libraries/", json=sample_library_data)

    updated_library_data = {
        "name": "Updated Sample Library",
    }

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.put(f"/libraries/{id}", json=updated_library_data)
    assert response.status_code == 200
    assert json.loads(response.data)["name"] == "Updated Sample Library"


def test_delete_library(client, sample_library_data):
    response = client.post("/libraries/", json=sample_library_data)

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.delete(f"/libraries/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "Library deleted successfully"
