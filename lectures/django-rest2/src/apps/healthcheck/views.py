from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View


@login_required
def healthcheck_view(request, pk=None):
    """
    :param request: User request
    :return: simple text
    """
    if request.method == 'GET':
        return HttpResponse("OK", status=200)

    return HttpResponse(status=405)


class HealthcheckView(View):
    resp_template = 'My status: {}'

    def get(self, request):
        return HttpResponse(self.resp_template.format("OK"), status=200)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, pk=None):
        pass
