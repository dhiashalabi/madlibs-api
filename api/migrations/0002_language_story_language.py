# Generated by Django 4.2a1 on 2023-02-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
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
                ("code", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="story",
            name="language",
            field=models.ManyToManyField(to="api.language"),
        ),
    ]