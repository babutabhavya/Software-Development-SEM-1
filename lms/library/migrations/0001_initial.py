# Generated by Django 4.2.9 on 2024-01-19 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Library",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="Libraries", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
