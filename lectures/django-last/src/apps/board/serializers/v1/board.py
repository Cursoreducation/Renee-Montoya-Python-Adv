from rest_framework import serializers

from src.apps.board.models import Board
from src.apps.board.serializers.v1.column import ColumnSerializer
from src.apps.users.serializers.v1.users import TrelloUserSerializer


class BoardSerializer(serializers.Serializer):
    name = serializers.CharField()
    favorite = serializers.BooleanField(default=False, required=False)
    columns = ColumnSerializer(many=True, read_only=True, source='column_set')
    owner = TrelloUserSerializer()
    participants = TrelloUserSerializer(many=True)

    def create(self, validated_data: dict) -> Board:
        return Board.objects.create(**validated_data)

    def update(self, instance: Board, validated_data: dict) -> Board:
        instance.name = validated_data.get('name', instance.name)
        instance.favorite = validated_data.get('favorite', instance.favorite)
        instance.save()
        return instance
