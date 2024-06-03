# Generated by Django 5.0.6 on 2024-06-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="State",
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
                ("Name", models.CharField(max_length=100)),
                ("Population", models.BigIntegerField()),
                ("Language", models.CharField(max_length=100)),
                ("Capital", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "State",
            },
        ),
    ]