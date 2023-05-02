from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # traemos los archivos media


urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('items.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
