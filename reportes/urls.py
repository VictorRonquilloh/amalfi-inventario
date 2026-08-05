from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('reportes/villa/', views.reporte_por_villa, name='por_villa'),
    path('reportes/manzana/', views.reporte_por_manzana, name='por_manzana'),
    path('reportes/kardex/', views.lista_kardex, name='lista_kardex'),
    path('reportes/kardex/<int:producto_id>/', views.kardex_producto, name='kardex_producto'),
    path('reportes/kardex-villas/', views.lista_kardex_villas, name='lista_kardex_villas'),
    path('reportes/kardex-villas/<int:villa_id>/', views.kardex_villa, name='kardex_villa'),
]
