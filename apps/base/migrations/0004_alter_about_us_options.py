# Generated by Django 5.1 on 2024-08-13 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_about_us"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about_us",
            options={"verbose_name": "", "verbose_name_plural": "Настройки о нас"},
        ),
    ]