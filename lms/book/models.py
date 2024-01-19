from django.contrib.auth import get_user_model
from django.db import models
from library.models import Library


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Borrowed By",
    )
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
