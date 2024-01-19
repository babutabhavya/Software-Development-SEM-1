from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Library
from .serializers import (
    LibrarySerializer,
    LibraryUserDeregistrationSerializer,
    LibraryUserRegistrationSerializer,
)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def perform_create(self, serializer):
        serializer.save(users=[])


class LibraryUserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LibraryUserRegistrationSerializer(
            data={
                "user_id": request.data.get("user_id"),
                "library_id": kwargs.get("library_id"),
            }
        )
        if serializer.is_valid():
            library = serializer.save()
            return Response(
                LibrarySerializer(library).data, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryUserDeregistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LibraryUserDeregistrationSerializer(
            data={
                "user_id": request.data.get("user_id"),
                "library_id": kwargs.get("library_id"),
            }
        )
        serializer.is_valid(raise_exception=True)

        library = serializer.update(serializer.validated_data)

        return Response(LibrarySerializer(library).data, status=status.HTTP_200_OK)
