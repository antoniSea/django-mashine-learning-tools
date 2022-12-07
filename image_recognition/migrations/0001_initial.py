# Generated by Django 4.1.1 on 2022-12-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("image", models.ImageField(upload_to="images/")),
                ("label", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
