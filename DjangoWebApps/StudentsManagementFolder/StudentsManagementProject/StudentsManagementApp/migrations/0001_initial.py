# Generated by Django 5.0.6 on 2024-05-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("phoneno", models.BigIntegerField()),
                ("currenttime", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Students",
            },
        ),
    ]