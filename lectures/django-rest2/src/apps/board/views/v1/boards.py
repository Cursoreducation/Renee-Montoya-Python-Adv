from rest_framework import generics

from src.apps.board.models import Board
from src.apps.board.serializers.v1.board import BoardSerializer


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.active()
    serializer_class = BoardSerializer

