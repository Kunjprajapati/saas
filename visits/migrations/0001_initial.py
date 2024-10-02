# Generated by Django 5.0.7 on 2024-10-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="visitsModel",
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
                ("timing", models.DateTimeField(auto_created=True)),
                ("path", models.TextField(null=True)),
            ],
        ),
    ]
