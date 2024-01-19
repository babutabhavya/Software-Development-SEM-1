from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.filter(
        is_active=True, is_staff=False, is_superuser=False
    )

    def perform_create(self, serializer):
        serializer.save(is_active=True)
