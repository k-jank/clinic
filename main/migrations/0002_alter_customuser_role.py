# Generated by Django 5.0.7 on 2024-08-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("dokter", "Dokter"),
                    ("padien", "Pasien"),
                ],
                default="dokter",
                max_length=10,
            ),
        ),
    ]