from django.urls import path
from . import views

app_name = 'ubicaciones'

urlpatterns = [
    path('ubicaciones/', views.lista_ubicaciones, name='lista_ubicaciones'),
]