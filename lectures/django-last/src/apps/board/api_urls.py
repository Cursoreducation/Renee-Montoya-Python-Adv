from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.apps.board.api_views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView
from src.apps.board.views.v1.boards import BoardListCreateAPIView
from src.apps.board.views.v1.columns import ColumnsModelViewSet

app_name = 'board'

router = DefaultRouter()
router.register('columns', ColumnsModelViewSet)

urlpatterns = [
    path('tasks/comments', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('tasks/comments/<int:comment_id>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('', BoardListCreateAPIView.as_view(), name='board-list-create'),
    path('', include(router.urls)),
]
