from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Library


class LibrarySerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=get_user_model().objects.all(), required=False
    )

    class Meta:
        model = Library
        fields = "__all__"
