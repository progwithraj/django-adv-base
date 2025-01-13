# Generated by Django 5.1.4 on 2025-01-13 15:35

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Address of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='author',
            field=models.BooleanField(default=False, verbose_name='if this profile is an Author'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Bio of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='IN', max_length=2, null=True, verbose_name='Country of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook link of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(blank=True, default='defaults/default_user_profile.png', null=True, upload_to='profile_images/', verbose_name='Image of the user profile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active status of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='jone_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Joined date of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateField(auto_now=True, null=True, verbose_name='Last login date of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Pincode of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter link of the user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User of this profile'),
        ),
    ]
