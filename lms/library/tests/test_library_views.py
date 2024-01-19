import pytest
from rest_framework import status

from library.models import Library


@pytest.fixture
def library_data():
    return {"name": "Test Library", "location": "Test Location"}


@pytest.fixture
def user_data():
    return {"username": "test_user", "password": "test", "name": "Test"}


@pytest.fixture
def create_library(client, library_data):
    response = client.post("/libraries/", library_data)
    return response.json()


@pytest.fixture
def create_user(client, user_data):
    response = client.post("/users/", user_data)
    return response.json()


@pytest.mark.django_db
def test_library_viewset_create(client, library_data):
    response = client.post("/libraries/", library_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Library.objects.filter(name="Test Library").exists()


@pytest.mark.django_db
def test_library_viewset_get(client, create_library):
    library_id = create_library["id"]
    response = client.get(f"/libraries/{library_id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == library_id
    assert response.data["name"] == "Test Library"
    assert response.data["location"] == "Test Location"


@pytest.mark.django_db
def test_library_viewset_update(client, create_library):
    library_id = create_library["id"]
    updated_data = {"name": "Updated Library", "location": "Updated Location"}
    response = client.put(
        f"/libraries/{library_id}/", data=updated_data, content_type="application/json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == library_id
    assert response.data["name"] == "Updated Library"
    assert response.data["location"] == "Updated Location"


@pytest.mark.django_db
def test_library_viewset_delete(client, create_library):
    library_id = create_library["id"]
    response = client.delete(f"/libraries/{library_id}/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Library.objects.filter(id=library_id).exists()


@pytest.mark.django_db
def test_library_user_registration_api_view_valid_data(
    client, create_library, create_user
):
    library_id = create_library["id"]
    user_id = create_user["id"]

    data = {"user_id": user_id, "library_id": library_id}
    response = client.post(f"/libraries/{library_id}/register-user/", data)

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert "name" in response.data


@pytest.mark.django_db
def test_library_user_registration_api_view_invalid_data(client, create_library):
    library_id = create_library["id"]

    data = {"user_id": 999, "library_id": library_id}
    response = client.post(f"/libraries/{library_id}/register-user/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_library_user_registration_api_view_library_not_found(client):
    library_id = 999

    data = {"user_id": 1, "library_id": library_id}
    response = client.post(f"/libraries/{library_id}/register-user/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_library_user_registration_api_view_user_not_found(client, create_library):
    library_id = create_library["id"]

    data = {"user_id": 999, "library_id": library_id}
    response = client.post(f"/libraries/{library_id}/register-user/", data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def create_library(client, library_data):
    response = client.post("/libraries/", library_data)
    return response.json()


@pytest.fixture
def create_user(client, user_data):
    response = client.post("/users/", user_data)
    return response.json()


@pytest.mark.django_db
def test_library_user_deregistration_api_view_valid_data(
    client, create_library, create_user
):
    library_id = create_library["id"]
    user_id = create_user["id"]

    print("User id", user_id)

    client.post(
        f"/libraries/{library_id}/register-user/", {"user_id": user_id}, format="json"
    )

    response = client.post(
        f"/libraries/{library_id}/deregister-user/", {"user_id": user_id}, format="json"
    )
    print(response.data)

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    assert "name" in response.data

    library = Library.objects.get(id=library_id)
    assert user_id not in library.users.values_list("id", flat=True)


@pytest.mark.django_db
def test_library_user_deregistration_api_view_invalid_user(client, create_library):
    library_id = create_library["id"]

    response = client.post(
        f"/libraries/{library_id}/deregister-user/", {"user_id": "999"}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_library_user_deregistration_api_view_invalid_library(client):
    response = client.post(f"/libraries/999/deregister-user/", {"user_id": "1"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
