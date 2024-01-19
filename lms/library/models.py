from django.contrib.auth import get_user_model
from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    users = models.ManyToManyField(get_user_model(), related_name="Libraries")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"
