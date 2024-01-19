from rest_framework import serializers
from .models import Library
from django.contrib.auth import get_user_model


class LibrarySerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=get_user_model().objects.all(), required=False
    )

    class Meta:
        model = Library
        fields = "__all__"
