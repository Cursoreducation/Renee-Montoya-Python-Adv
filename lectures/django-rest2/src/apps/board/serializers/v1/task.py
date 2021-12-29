from rest_framework import serializers

from src.apps.board.models import Task
from src.apps.board.serializers.v1.comment import CommentSerializer
from src.apps.users.models import TrelloUser


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    created_by = serializers.IntegerField(source='created_by_id', read_only=True)

    def get_comments_count(self, instance: Task) -> int:
        # TODO optimize query
        return instance.comments.count()

    class Meta:
        model = Task
        fields = ['name', 'column', 'created_by', 'comments', 'comments_count']
