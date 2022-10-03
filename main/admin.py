from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.News)
admin.site.register(models.Events)
admin.site.register(models.BrgyOfficials)
admin.site.register(models.SkOfficials)