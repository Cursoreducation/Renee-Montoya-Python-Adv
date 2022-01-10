from rest_framework import serializers

from src.apps.board.models import Comment, Task
from src.apps.users.models import TrelloUser
from src.apps.users.serializers.v1.users import TrelloUserSerializer


class CommentSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    # owner = serializers.PrimaryKeyRelatedField(required=True, queryset=TrelloUser.objects.all())
    owner = TrelloUserSerializer()
    # task = serializers.IntegerField(required=True)
    task = serializers.PrimaryKeyRelatedField(required=True, queryset=Task.objects.active())

    # def validate_task(self, task_id):
    #     try:
    #         task = Task.objects.active().get(id=task_id)
    #         return task
    #     except Task.DoesNotExist:
    #         raise ValidationError(f"Task does not exist: {task_id}")

    def create(self, validated_data: dict) -> Comment:
        # comment = Comment.objects.create(**validated_data)
        # comment.save()
        return Comment.objects.create(**validated_data)

    def update(self, instance: Comment, validated_data: dict) -> Comment:
        instance.message = validated_data.get('message', instance.message)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.task = validated_data.get('task', instance.task)
        instance.save()
        return instance
