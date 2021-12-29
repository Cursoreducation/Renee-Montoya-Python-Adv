from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def healthcheck_api_view(request):
    return Response(data={'status': 'OK'}, status=status.HTTP_200_OK)

