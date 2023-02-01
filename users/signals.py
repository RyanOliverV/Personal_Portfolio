from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#Once a user is created, this function receives that information and then creates a profile for the user#
#Using @reciever that is found in documentation here: https://docs.djangoproject.com/en/4.1/topics/signals/
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#This function saves the profile information after it's been updated
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()