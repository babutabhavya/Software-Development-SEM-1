from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets, status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
