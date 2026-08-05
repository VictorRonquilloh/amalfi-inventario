from django.contrib import admin
from .models import Entrada, Salida


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'no_comprobante', 'producto', 'cantidad', 'precio_compra', 'usuario']
    list_filter = ['fecha', 'producto__categoria']
    date_hierarchy = 'fecha'


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'no_comprobante', 'producto', 'cantidad', 'villa', 'precio', 'total_gastado', 'usuario']
    list_filter = ['fecha', 'producto__categoria']
    date_hierarchy = 'fecha'
