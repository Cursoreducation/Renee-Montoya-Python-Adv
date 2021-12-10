from django.contrib import admin

# Register your models here.
from src.apps.board.models import Board, Comment, Task

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Comment)
