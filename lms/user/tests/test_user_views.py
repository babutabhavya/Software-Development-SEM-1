import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user_data():
    return {"username": "testuser", "password": "testpassword"}


@pytest.mark.django_db
def test_create_user(api_client, test_user_data):
    response = api_client.post(reverse("user-list"), test_user_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert get_user_model().objects.filter(username="testuser").exists()


@pytest.mark.django_db
def test_update_user(api_client, test_user_data):
    user = get_user_model().objects.create(
        username="existinguser", password="testpassword"
    )
    url = reverse("user-detail", args=[user.id])

    response = api_client.put(url, test_user_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert get_user_model().objects.filter(username="testuser").exists()
    assert not get_user_model().objects.filter(username="existinguser").exists()


@pytest.mark.django_db
def test_delete_user(api_client, test_user_data):
    user = get_user_model().objects.create(
        username="existinguser", password="testpassword"
    )
    url = reverse("user-detail", args=[user.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not get_user_model().objects.filter(username="existinguser").exists()
