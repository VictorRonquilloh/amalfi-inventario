from django.contrib import admin
from .models import Urbanizacion, Manzana, Villa


@admin.register(Urbanizacion)
class UrbanizacionAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Manzana)
class ManzanaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'urbanizacion']
    list_filter = ['urbanizacion']


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'manzana']
    list_filter = ['manzana']
