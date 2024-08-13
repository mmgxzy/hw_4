# Generated by Django 5.1 on 2024-08-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_about_us_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="image2/", verbose_name="Фото")),
            ],
            options={
                "verbose_name_plural": "Фотография",
            },
        ),
    ]