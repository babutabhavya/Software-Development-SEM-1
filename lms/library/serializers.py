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


class LibraryUserRegistrationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    library_id = serializers.IntegerField()

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        library_id = attrs.get("library_id")

        try:
            library = Library.objects.get(id=library_id)
        except Library.DoesNotExist as exc:
            raise serializers.ValidationError({"error": "Library not found"}) from exc

        try:
            user = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist as exc:
            raise serializers.ValidationError({"error": "User not found"}) from exc

        if user in library.users.all():
            raise serializers.ValidationError(
                {"error": "User is already in the library"}
            )

        attrs["library"] = library
        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        library = validated_data.get("library")
        user = validated_data.get("user")

        library.users.add(user)
        return library

    def update(self, instance, validated_data):
        pass


class LibraryUserDeregistrationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    library_id = serializers.IntegerField()

    def validate(self, attrs):
        user_id = attrs.get("user_id")
        library_id = attrs.get("library_id")

        try:
            library = Library.objects.get(id=library_id)
        except Library.DoesNotExist as exc:
            raise serializers.ValidationError({"error": "Library not found"}) from exc

        try:
            user = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist as exc:
            raise serializers.ValidationError({"error": "User not found"}) from exc

        if user not in library.users.all():
            raise serializers.ValidationError({"error": "User is not in the library"})

        attrs["library"] = library
        attrs["user"] = user
        return attrs

    def update(self, validated_data, *args):
        library = validated_data.get("library")
        user = validated_data.get("user")

        library.users.remove(user)
        library.save()
        return library

    def create(self, *args):
        pass
