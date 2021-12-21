from django.contrib import admin

# Register your models here.
from src.apps.board.models import Board, Column, Comment, Task


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'favorite')
    fields = ('id', 'name')


admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Column)
