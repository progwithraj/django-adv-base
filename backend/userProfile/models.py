from customUser.models import CustomUser
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_("User of this profile"),
        related_name="profile",
    )
    image = models.FileField(
        upload_to="profile_images/",
        default="defaults/default_user_profile.png",
        null=True,
        blank=True,
        verbose_name=_("Image of the user profile"),
    )
    author = models.BooleanField(
        default=False, verbose_name=_("if this profile is an Author")
    )
    bio = models.TextField(null=True, blank=True, verbose_name=_("Bio of the user"))
    address = models.TextField(
        max_length=100, null=True, blank=True, verbose_name=_("Address of the user")
    )
    pincode = models.CharField(
        max_length=6, null=True, blank=True, verbose_name=_("Pincode of the user")
    )
    country = CountryField(
        blank_label="(select country)",
        null=True,
        blank=True,
        default="IN",
        verbose_name=_("Country of the user"),
    )
    facebook = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("Facebook link of the user"),
    )
    twitter = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("Twitter link of the user"),
    )
    jone_date = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_("Joined date of the user"),
    )
    last_login = models.DateField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=_("Last login date of the user"),
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_("Active status of the user")
    )

    def __str__(self):
        return self.user.username
