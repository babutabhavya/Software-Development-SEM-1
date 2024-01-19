import json
import pytest
from src.app import app
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
def sample_user_data():
    return {
        "email": "user@example.com",
        "full_name": "John Doe",
    }


@pytest.fixture
def client(test_app):
    return test_app.test_client()


def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert json.loads(response.data) == []


def test_add_user(sample_user_data, client):
    response = client.post("/users/", json=sample_user_data)
    assert response.status_code == 201
    assert json.loads(response.data)["full_name"] == "John Doe"


def test_get_user(test_app, sample_user_data):
    client = test_app.test_client()
    response = client.post("/users/", json=sample_user_data)
    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.get(f"/users/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["full_name"] == "John Doe"


def test_update_user(client, sample_user_data):
    response = client.post("/users/", json=sample_user_data)

    updated_user_data = {
        "email": "updated_user@example.com",
        "full_name": "Updated John Doe",
    }

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.put(f"/users/{id}", json=updated_user_data)
    assert response.status_code == 200
    assert json.loads(response.data)["full_name"] == "Updated John Doe"


def test_delete_user(client, sample_user_data):
    response = client.post("/users/", json=sample_user_data)

    assert response.status_code == 201

    id = json.loads(response.data)["id"]

    response = client.delete(f"/users/{id}")
    assert response.status_code == 200
    assert json.loads(response.data)["message"] == "User deleted successfully"
