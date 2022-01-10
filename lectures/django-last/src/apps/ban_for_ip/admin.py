from django.contrib import admin

# Register your models here.
from src.apps.ban_for_ip.models import BannedIP


@admin.register(BannedIP)
class BannedIPModelAdmin(admin.ModelAdmin):
    pass
