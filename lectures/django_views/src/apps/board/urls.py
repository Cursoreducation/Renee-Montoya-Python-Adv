
from django.urls import path

from src.apps.board.views import BoardDetailView

app_name = 'board'

urlpatterns = [
    path('<int:pk>/', BoardDetailView.as_view(), name='detail'),
]
