from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'descripcion', 'categoria', 'unidad', 'precio_compra', 'precio_venta', 'existencia']
    search_fields = ['codigo', 'descripcion']
    list_filter = ['categoria', 'unidad']