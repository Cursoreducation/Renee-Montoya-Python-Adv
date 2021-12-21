
from django.urls import path

from src.apps.board.views import BoardDetailView, BoardListView, TaskCreateView, boards_list_api_view

app_name = 'board'

urlpatterns = [
    path('api/list', boards_list_api_view, name='api-list'),
    path('<int:pk>/', BoardDetailView.as_view(), name='detail'),
    path('<int:pk>/tasks/create', TaskCreateView.as_view(), name='task-create'),
    path('', BoardListView.as_view(), name='list')
]
