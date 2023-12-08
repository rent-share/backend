# Generated by Django 5.0 on 2023-12-08 17:37

import accommodation.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accommodation", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="rental_type",
            field=models.IntegerField(
                choices=[(1, "Month-to-Month"), (2, "6 Months Lease"), (3, "1 Year Lease")], default=1
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Flat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_approved", models.BooleanField(default=False, editable=False)),
                ("approved_at", models.DateTimeField(auto_now_add=True)),
                ("is_pinned", models.BooleanField(default=False, editable=False)),
                ("pinned_at", models.DateTimeField(auto_now_add=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("province", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("max_occupancy", models.PositiveIntegerField()),
                ("rent_price", models.PositiveIntegerField(help_text="Price per month in Nepali Rupees")),
                ("availability_calendar", models.DateField()),
                ("floor_level", models.PositiveIntegerField()),
                ("is_booked", models.BooleanField(default=False)),
                (
                    "rental_type",
                    models.IntegerField(
                        choices=[(1, "Month-to-Month"), (2, "6 Months Lease"), (3, "1 Year Lease")]
                    ),
                ),
                (
                    "square_footage",
                    models.CharField(
                        blank=True,
                        help_text="Width x Length in feet",
                        max_length=255,
                        validators=[accommodation.validators.validate_dimension_format],
                    ),
                ),
                ("tv", models.BooleanField(default=False)),
                ("wifi", models.BooleanField(default=False)),
                ("air_conditioning", models.BooleanField(default=False)),
                ("laundry", models.BooleanField(default=False)),
                ("room_cleaning", models.BooleanField(default=False)),
                (
                    "parking_facility",
                    models.IntegerField(
                        choices=[(1, "Two Wheeler"), (2, "Four Wheeler"), (3, "Both"), (4, "None")], default=4
                    ),
                ),
                ("available_furnishings", models.CharField(blank=True, max_length=255)),
                ("bathroom_type", models.IntegerField(choices=[(1, "Attached"), (2, "Shared")])),
                ("with_shower", models.BooleanField(default=False)),
                ("with_bathtub", models.BooleanField(default=False)),
                ("wheelchair_accessible", models.BooleanField(default=False)),
                ("elevator_access", models.BooleanField(default=False)),
                ("pets_allowed", models.BooleanField(default=False)),
                ("smoking_allowed", models.BooleanField(default=False)),
                ("only_couples_allowed", models.BooleanField(default=False)),
                (
                    "age_restriction",
                    models.PositiveIntegerField(blank=True, help_text="Minimum age in years", null=True),
                ),
                ("security_guard", models.BooleanField(default=False)),
                ("cctv", models.BooleanField(default=False)),
                ("fire_alarm", models.BooleanField(default=False)),
                ("fire_extinguisher", models.BooleanField(default=False)),
                ("insurance_details", models.TextField(blank=True)),
                ("nearby_points_of_interest", models.TextField(blank=True)),
                ("proximity_to_public_transport", models.CharField(blank=True, max_length=255)),
                (
                    "noise_level",
                    models.IntegerField(
                        choices=[
                            (1, "Very Quiet"),
                            (2, "Quiet"),
                            (3, "Moderate"),
                            (4, "Loud"),
                            (5, "Very Loud"),
                        ],
                        default=4,
                    ),
                ),
                ("owner_full_name", models.CharField(max_length=255)),
                (
                    "owner_contact_number",
                    models.CharField(
                        max_length=10, validators=[accommodation.validators.validate_nepali_phone_number]
                    ),
                ),
                ("my_own_asset", models.BooleanField(default=False, help_text="Check if you own the asset.")),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text='Descriptive name for the flat (e.g., "Modern Studio in Trendy Neighborhood", "Spacious Family Flat with Balcony"). ',
                        max_length=255,
                    ),
                ),
                ("no_of_bedrooms", models.PositiveIntegerField()),
                ("no_of_bathrooms", models.PositiveIntegerField()),
                ("with_kitchen", models.BooleanField(default=True)),
                (
                    "building_type",
                    models.IntegerField(
                        choices=[(1, "Apartment"), (2, "House"), (3, "Hotel"), (4, "Loft"), (5, "Hostel")]
                    ),
                ),
                ("year_built", models.IntegerField()),
                ("is_furnished", models.BooleanField(default=False)),
                ("security_deposit", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "approved_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="approved_%(class)s",
                        to=settings.AUTH_USER_MODEL,
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
                    "pinned_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pinned_%(class)s",
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
                "abstract": False,
            },
        ),
    ]