from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class AuthToken(ObtainAuthToken):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
