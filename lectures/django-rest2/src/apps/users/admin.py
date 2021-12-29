from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from src.apps.users.models import TrelloUser


@admin.register(TrelloUser)
class TrelloUserModelAdmin(UserAdmin):
    pass
