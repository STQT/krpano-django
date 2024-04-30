# django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# project core app
from apps.core.swagger import urlpatterns as doc_urls
urlpatterns = doc_urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('apps.city.urls')),
    path('', include('apps.place.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)