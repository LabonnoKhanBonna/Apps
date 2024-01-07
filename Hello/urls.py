from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
admin.site.site_header = "Icecream Admin"
admin.site.site_title = "Icecream Admin Portal"
admin.site.index_title = "Welcome to Icecream"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_URL)
