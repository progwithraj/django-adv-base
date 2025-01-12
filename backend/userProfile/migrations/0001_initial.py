# Generated by Django 5.1.4 on 2025-01-12 19:33

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='defaults/default_user_profile.png', null=True, upload_to='profile_images/')),
                ('author', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, default='IN', max_length=2, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('jone_date', models.DateField(auto_now_add=True, null=True)),
                ('last_login', models.DateField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]