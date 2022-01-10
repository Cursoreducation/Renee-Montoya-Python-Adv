from django.urls import path

from src.apps.healthcheck.views import HealthcheckView, healthcheck_view

app_name = 'healthcheck'

urlpatterns = [
    path('healthcheck/', healthcheck_view, name='healthcheck_view'),
    # path('healthcheck/', HealthcheckView.as_view(), name='healthcheck_view'),
]
