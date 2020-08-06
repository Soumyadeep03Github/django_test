from django.contrib import admin
from .models import user, activity_periods

# Register your models here.

admin.site.register(user)
admin.site.register(activity_periods)