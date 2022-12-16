from django.contrib import admin
from .models import Profiles, Reports, Requests, Messages, SendMessages, Verificationss, WalkInProfiles, WalkInRequests
# Register your models here.

admin.site.register(Profiles)
admin.site.register(WalkInProfiles)
admin.site.register(Reports)
admin.site.register(Requests)
admin.site.register(WalkInRequests)
admin.site.register(Messages)
admin.site.register(SendMessages)
admin.site.register(Verificationss)