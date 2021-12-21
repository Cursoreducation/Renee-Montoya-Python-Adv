from rest_framework import serializers

from src.apps.board.models import Task
from src.apps.board.serializers.v1.comment import CommentSerializer


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, instance: Task) -> int:
        # TODO optimize query
        return instance.comments.count()

    class Meta:
        model = Task
        fields = ['name', 'column', 'created_by', 'comments']
