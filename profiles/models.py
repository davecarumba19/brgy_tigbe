from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profiles(models.Model):
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default profile.jpg')
    username = models.CharField(max_length=500, null=True, blank=True)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500, null=True, blank=True, choices=GENDER)
    address = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username


class Reports(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class Requests(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)