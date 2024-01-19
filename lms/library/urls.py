from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    LibraryUserDeregistrationAPIView,
    LibraryUserRegistrationAPIView,
    LibraryViewSet,
)

router = DefaultRouter()
router.register(r"", LibraryViewSet, basename="library")

urlpatterns = [
    path(
        "<int:library_id>/register-user/",
        LibraryUserRegistrationAPIView.as_view(),
        name="register-user",
    ),
    path(
        "<int:library_id>/deregister-user/",
        LibraryUserDeregistrationAPIView.as_view(),
        name="deregister-user",
    ),
    path("", include(router.urls)),
]
