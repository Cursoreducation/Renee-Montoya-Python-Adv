from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.board.models import Comment
from src.apps.board.permissions import IsOwnerOrReadOnly
from src.apps.board.serializers.v1.comment import CommentSerializer


class CommentAPIView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self, pk: int):
        try:
            comment = Comment.objects.get(id=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, comment_id: int) -> Response:
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(instance=comment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self):
        # data = dict(self.request.data)
        # data['task'] = task_id

        serializer = CommentSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # comment = serializer.save()
        # TODO check if serializer data has been updated
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, comment_id: int):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _perform_update(self, comment, data, partial=False):
        serializer = CommentSerializer(instance=comment, data=self.request.data, partial=partial)
        serializer.save()
        return serializer.data

    def put(self, comment_id: int):
        comment = self.get_object(comment_id)
        data = self._perform_update(comment, self.request.data)
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, comment_id: int):
        comment = self.get_object(comment_id)
        data = self._perform_update(comment, self.request.data, partial=True)
        return Response(data=data, status=status.HTTP_200_OK)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # POST/GET list
    # /boards/tasks/comments
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # GET/ PUT / PATCH / DELETE
    # /boards/tasks/comments/{id}
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return self.queryset.select_related('owner')
