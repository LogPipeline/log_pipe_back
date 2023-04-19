from django.contrib import admin
from .models import *


@admin.register(AdminUser)
class UserAdmin(admin.ModelAdmin):
    pass