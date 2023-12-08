# Generated by Django 5.0 on 2023-12-08 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("util", "0002_alter_media_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to={"model__in": ("room", "review", "qanda")},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="media",
                to="contenttypes.contenttype",
            ),
        ),
    ]
