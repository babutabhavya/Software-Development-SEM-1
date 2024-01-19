from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import BookViewSet

router = DefaultRouter()
router.register(r"", BookViewSet, basename="books")

urlpatterns = [
    path("", include(router.urls)),
]
