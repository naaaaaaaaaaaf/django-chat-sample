from django.conf import settings
from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name='ルーム名')
    created_at = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='room_owner'
    )
