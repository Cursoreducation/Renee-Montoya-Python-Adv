from django.conf import settings
from django.db import models

# Create your models here.
from src.apps.users.models import TrelloUser
from src.common.models import BaseDateAuditModel


class Board(BaseDateAuditModel):
    name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Name"
    )
    owner = models.ForeignKey(
        # to=TrelloUser,
        # to='users.TrelloUser',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='boards'
    )
    participants = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL
    )
    # user = TrelloUser.objects.last()
    # user.boards.all()
    favorite = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            ('name', 'owner')
        ]


class Column(BaseDateAuditModel):
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name="Name"
    )
    board = models.ForeignKey(
        to='Board',
        on_delete=models.SET_NULL,
        null=True
    )
    order = models.PositiveSmallIntegerField(default=0)


class Task(BaseDateAuditModel):
    name = models.CharField(max_length=255)
    column = models.ForeignKey(
        to='Column',
        on_delete=models.SET_NULL,
        null=True
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='tasks'
    )


class Comment(BaseDateAuditModel):
    message = models.TextField()
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='comments'
    )

