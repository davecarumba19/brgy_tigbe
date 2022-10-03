from django.db import models
import uuid
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default thumbnail.png')
    location = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default thumbnail.png')
    location = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class BrgyOfficials(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    position = models.CharField(max_length=1000, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default profile.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.position

class SkOfficials(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    position = models.CharField(max_length=1000, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default profile.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.position



