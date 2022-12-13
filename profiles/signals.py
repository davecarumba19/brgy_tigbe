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
            phone_number=user.phone_number,
            blk_unit=user.blk_unit,
            phase_street=user.phase_street,
            status=user.status,
            gender=user.gender,
            vaccine=user.vaccine,
            village=user.village,
            profile_image=user.profile_image,
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
        