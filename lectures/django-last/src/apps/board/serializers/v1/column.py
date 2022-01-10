from rest_framework import serializers
from src.apps.board.serializers.v1.task import TaskSerializer

from src.apps.board.models import Column


class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Column
        fields = ('name', 'order', 'tasks', 'board')
        extra_kwargs = {
            'board': {'write_only': True},
            'tasks': {'read_only': True, 'required': False}
        }
