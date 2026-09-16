from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Amalfi - Sistema de Gestión de Inventarios"
admin.site.site_title = "Amalfi Admin"
admin.site.index_title = "Bienvenido al sistema de gestión de inventarios de Amalfi"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('catalogo.urls')),
    path('', include('movimientos.urls')),
    path('', include('ubicaciones.urls')),
    path('', include('reportes.urls')),
]