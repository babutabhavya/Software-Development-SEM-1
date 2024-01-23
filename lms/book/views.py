from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Book objects.

    Attributes:
        queryset (QuerySet): The set of Book objects to be used in the view.
        serializer_class (Serializer): The serializer class for Book objects.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
