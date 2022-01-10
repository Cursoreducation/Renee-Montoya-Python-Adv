from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from src.apps.ban_for_ip.utils import default_ban_time, refresh_banned_ips


# Create your models here.


class BannedIP(models.Model):
    ip = models.GenericIPAddressField()
    expire_date = models.DateTimeField(default=default_ban_time)

    # def save(self, **kwargs):
    #     super().save(**kwargs)
    #     refresh_banned_ips()

    def __str__(self):
        return f'{self.ip}: for {(self.expire_date - timezone.now()).days}'


post_save.connect(refresh_banned_ips, sender=BannedIP)
