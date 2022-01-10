from django.db.models import Count, Prefetch
from rest_framework import generics

from src.apps.board.models import Board, Comment, Task
from src.apps.board.serializers.v1.board import BoardSerializer


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.active()
    serializer_class = BoardSerializer

    def get_queryset(self):
        prefetch_tasks = Prefetch(
            'column_set__tasks',
            queryset=Task.objects.select_related('column', 'created_by') \
                .prefetch_related(Prefetch('comments', queryset=Comment.objects.select_related('owner'))) \
                .annotate(comments_count=Count('comments'))
        )
        return super().get_queryset() \
            .select_related('owner') \
            .prefetch_related('participants', 'column_set', prefetch_tasks)
