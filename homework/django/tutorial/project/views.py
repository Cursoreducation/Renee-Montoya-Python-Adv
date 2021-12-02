from django.http import HttpResponse
from random import randint


def status(request):
    return HttpResponse("ok")


def random_color(request):
    color = "#" + "%06x" % randint(0, 0xFFFFFF)
    return HttpResponse(color)
