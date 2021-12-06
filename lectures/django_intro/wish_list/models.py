from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User


class WishList(models.Model):
    # user = models.ForeignKey(to=User)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    wish = models.CharField(max_length=255)
