from django.urls import path
from . import views

app_name = 'movimientos'

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/nueva/', views.crear_entrada, name='crear_entrada'),
    path('salidas/', views.lista_salidas, name='lista_salidas'),
    path('salidas/nueva/', views.crear_salida, name='crear_salida'),
]
