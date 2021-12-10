from django.urls import path

from src.apps.homepage.views import HomePageView

app_name = 'homepage'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='homepage'),
    # path('healthcheck/', HealthcheckView.as_view(), name='healthcheck_view'),
]
