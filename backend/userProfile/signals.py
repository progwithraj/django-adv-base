from colorama import Fore
from customUser.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # only create user profile if user is created
        UserProfile.objects.create(user=instance)
        # set user to active
        CustomUser.objects.filter(id=instance.id).update(is_active=True)
        print(Fore.YELLOW + f"Profile created for user: {instance.username}")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    # save user profile to database
    instance.userprofile.save()
    print(Fore.GREEN + f"Profile updated for user: {instance.username}")
