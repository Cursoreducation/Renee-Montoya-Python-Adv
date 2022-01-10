import pytest

from src.apps.board.models import Comment
from src.apps.board.serializers.v1.comment import CommentSerializer
from tests.factories.boards import CommentFactory, TaskFactory
from tests.factories.users import TrelloUserFactory


class TestComments:

    @pytest.mark.django_db
    def test_comment_validation(self):
        task = TaskFactory()
        user = TrelloUserFactory()
        data = {
            'owner': user.id,
            'task': task.id,
            'message': 'bla bla'
        }
        serializer = CommentSerializer(data=data)
        assert serializer.is_valid()

    @pytest.mark.django_db
    def test_comment_validation_error(self):
        task = TaskFactory()
        data = {
            'owner': 42,
            'task': task.id,
            'message': 'bla bla'
        }
        serializer = CommentSerializer(data=data)
        assert not serializer.is_valid()
        assert 'owner' in serializer.errors

    @pytest.mark.django_db
    def test_comment_validation_create(self):
        task = TaskFactory()
        user = TrelloUserFactory()
        data = {
            'owner': user.id,
            'task': task.id,
            'message': 'bla bla'
        }
        serializer = CommentSerializer(data=data)
        assert serializer.is_valid()

        assert Comment.objects.count() == 0

        serializer.save()
        assert Comment.objects.count() == 1

    @pytest.mark.django_db
    def test_comment_validation_update(self):
        comment = CommentFactory(message='14124124124')
        data = {
            'message': 'bla bla'
        }
        serializer = CommentSerializer(instance=comment, data=data, partial=True)
        assert serializer.is_valid()

        assert Comment.objects.count() == 1

        serializer.save()
        assert Comment.objects.count() == 1
        comment.refresh_from_db()

        assert comment.message == 'bla bla'
