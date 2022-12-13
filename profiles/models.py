from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profiles(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    VACCINE = (
        ('Vaccinated', 'Vaccinated'),
        ('Not Vaccinated', 'Not Vaccinated')
    )
    VILLAGE = (
        ('Crisville', 'Crisville'),
        ('Gulod', 'Gulod'),
        ('Matandang Barrio', 'Matandang Barrio'),
        ('Mataas na Kahoy', 'Mataas na Kahoy'),
        ('Katuparan', 'Katuparan'),
        ('Kaypiskal', 'Kaypiskal'),
        ('Sulucan', 'Sulucan'),
        ('NHV', 'NHV'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default profile.jpg')
    username = models.CharField(max_length=500, null=True, blank=True)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500, null=True, blank=True, choices=GENDER)
    vaccine = models.CharField(max_length=500, null=True, blank=True, choices=VACCINE)
    verified = models.BooleanField(default=False, null=True)
    blk_unit = models.CharField(max_length=500, null=True, blank=True)
    phase_street = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    village = models.CharField(max_length=500, null=True, blank=True, choices=VILLAGE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username


class WalkInProfiles(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    VACCINE = (
        ('Vaccinated', 'Vaccinated'),
        ('Not Vaccinated', 'Not Vaccinated')
    )
    VILLAGE = (
        ('Crisville', 'Crisville'),
        ('Gulod', 'Gulod'),
        ('Matandang Barrio', 'Matandang Barrio'),
        ('Mataas na Kahoy', 'Mataas na Kahoy'),
        ('Katuparan', 'Katuparan'),
        ('Kaypiskal', 'Kaypiskal'),
        ('Sulucan', 'Sulucan'),
        ('NHV', 'NHV'),
    )
    created_by = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default profile.jpg')
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500, null=True, blank=True, choices=GENDER)
    vaccine = models.CharField(max_length=500, null=True, blank=True, choices=VACCINE)
    verified = models.BooleanField(default=False, null=True)
    blk_unit = models.CharField(max_length=500, null=True, blank=True)
    phase_street = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    village = models.CharField(max_length=500, null=True, blank=True, choices=VILLAGE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.first_name

class Reports(models.Model):
    sender = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True, related_name='report')
    sender_username = models.CharField(max_length=1000, null=True, blank=True, editable=False)
    receiver_username = models.CharField(max_length=1000, null=True, blank=True, editable=False)
    location = models.CharField(max_length=1000, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    hide = models.BooleanField(default=False, null=True)
    done = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender.username+"'s report "

    class Meta:
        ordering = ['is_read', '-date_created']

class Requests(models.Model):

    DOCUMENT = (
        ('Brgy. Clearance', 'Brgy. Clearance'),
        ('Certificate of Indigency', 'Certificate of Indigency')
    )

    sender = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True, related_name='request')
    sender_username = models.CharField(max_length=1000, null=True, blank=True, editable=False)
    receiver_username = models.CharField(max_length=1000, null=True, blank=True, editable=False)
    document_type = models.CharField(max_length=1000, null=True, blank=True, choices=DOCUMENT)
    purpose = models.CharField(max_length=1000, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    hide = models.BooleanField(default=False, null=True)
    done = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender.username+"'s request"

    class Meta:
        ordering = ['is_read', '-date_created']


class Messages(models.Model):

    DOCUMENT = (
        ('Brgy. Clearance', 'Brgy. Clearance'),
        ('Certificate of Indigency', 'Certificate of Indigency')
    )

    sender = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True, related_name='message')
    document_type = models.CharField(max_length=1000, null=True, blank=True, choices=DOCUMENT)
    purpose = models.CharField(max_length=1000, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender.username+"'s message"

    class Meta:
        ordering = ['is_read', '-date_created']



class SendMessages(models.Model):

    sender = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True, related_name='send_message')
    message = models.TextField(max_length=1000, null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender.username+"'s message"



class Verificationss(models.Model):
    sender = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True, related_name='verification')
    brgy_id = models.ImageField(null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.sender.username+"'s verification"

    class Meta:
        ordering = ['is_read', '-date_created']

