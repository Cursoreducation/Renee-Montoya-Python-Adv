import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns_v1 = [
    path('', include('apps.healthcheck.api_urls')),
]

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/v1/', include(urlpatterns_v1)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('service/', include('apps.healthcheck.urls')),
    path('boards/', include('apps.board.urls')),
    path('', include('apps.homepage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
