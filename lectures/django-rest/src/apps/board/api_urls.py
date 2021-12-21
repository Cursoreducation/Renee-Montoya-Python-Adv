
from django.urls import path

from src.apps.board.api_views import CommentAPIView

app_name = 'board'

urlpatterns = [
    path('tasks/comments/<int:comment_id>', CommentAPIView.as_view(), name='task-create'),
]
