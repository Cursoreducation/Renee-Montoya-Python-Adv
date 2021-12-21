from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models import Count


class TrelloUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars')
