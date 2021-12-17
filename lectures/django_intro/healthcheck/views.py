from django.http import HttpResponse


# Create your views here.

def check_status(request):
    return HttpResponse("OK", status=200)
