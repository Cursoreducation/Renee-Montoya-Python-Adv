from rest_framework.viewsets import ModelViewSet

from src.apps.board.models import Column
from src.apps.board.serializers.v1.column import ColumnSerializer


class ColumnsModelViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
