from django.urls import path

from src.apps.healthcheck.api_views import healthcheck_api_view

app_name = 'healthcheck'

urlpatterns = [
    path('healthcheck/', healthcheck_api_view, name='healthcheck_api_view'),
    # path('healthcheck/', HealthcheckView.as_view(), name='healthcheck_view'),
]
