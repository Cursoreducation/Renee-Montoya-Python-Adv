from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin

from src.apps.ban_for_ip.utils import get_client_ip, is_banned_ip


class BanForIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # client_ip = get_client_ip(request)
        # '172.24.0.1'
        # banned_ips = cache.get(settings.BAN_FOR_IP_PREFIX)
        req_ip = get_client_ip(request)
        if is_banned_ip(req_ip):
            raise PermissionDenied()
