from rest_framework import viewsets

from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.filter(
        is_active=True, is_staff=False, is_superuser=False
    )
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(is_active=True)
