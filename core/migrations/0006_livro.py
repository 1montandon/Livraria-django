# Generated by Django 5.0.2 on 2024-03-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_autor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
    ]