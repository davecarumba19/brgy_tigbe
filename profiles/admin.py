from django.contrib import admin
from .models import Profiles, Reports, Requests, Messages
# Register your models here.

admin.site.register(Profiles)
admin.site.register(Reports)
admin.site.register(Requests)
admin.site.register(Messages)