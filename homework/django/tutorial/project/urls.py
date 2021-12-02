from django.urls import path
from .views import status, random_color


urlpatterns = [
    path('status/', status, name='status'),
    path('random_color/', random_color, name='random_color'),
]