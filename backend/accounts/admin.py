from django.contrib import admin
from .models import *



@admin.register(UserProfileInformation)
class UserAdmin(admin.ModelAdmin):
    pass