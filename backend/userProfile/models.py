from django.db import models
from customUser.models import CustomUser
from django_countries.fields import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(upload_to='profile_images/', default='defaults/default_user_profile.png' ,null=True, blank=True)
    author = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=6, null=True, blank=True)
    country = CountryField(blank_label='(select country)', null=True, blank=True, default='IN')
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    jone_date = models.DateField(auto_now_add=True, null=True, blank=True)
    last_login = models.DateField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username