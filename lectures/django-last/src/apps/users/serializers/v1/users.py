from rest_framework import serializers

from src.apps.users.models import TrelloUser


class TrelloUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='user_fullname')

    def user_fullname(self, instance: TrelloUser) -> str:
        return instance.get_full_name()

    class Meta:
        model = TrelloUser
        fields = ('username', 'full_name', 'id', 'avatar', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'avatar': {'required': False},
        }
