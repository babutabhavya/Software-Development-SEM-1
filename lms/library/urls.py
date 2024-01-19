from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LibraryViewSet

router = DefaultRouter()
router.register(r"", LibraryViewSet, basename="library")

urlpatterns = [
    path("", include(router.urls)),
]
