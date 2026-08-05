from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('catalogo.urls')),
    path('', include('movimientos.urls')),
    path('', include('ubicaciones.urls')),
    path('', include('reportes.urls')),
]

