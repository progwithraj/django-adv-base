# Generated by Django 5.1.4 on 2025-01-14 16:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("customUser", "0002_alter_customuser_managers"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="customuser",
            table="Users",
        ),
    ]