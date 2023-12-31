# Generated by Django 5.0 on 2023-12-28 16:25

import django.db.models.deletion
import media.models
import media.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "media",
                    models.FileField(
                        upload_to=media.models.get_media_upload_to_path,
                        validators=[
                            media.validators.validate_file_extension,
                            media.validators.validate_file_size,
                        ],
                    ),
                ),
                ("caption", models.CharField(blank=True, max_length=255)),
                ("alt_text", models.CharField(blank=True, max_length=255)),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        limit_choices_to={"model__in": ("room", "flat", "house", "review", "qanda")},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updated_%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
