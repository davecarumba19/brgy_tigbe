from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profiles
from django.dispatch import receiver

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )


@receiver(post_save, sender=Profiles)
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profiles)
def deleteProfile(sender, instance, **kwargs):
    try: 
        user = instance.user
        user.delete()
    except:
        pass
        