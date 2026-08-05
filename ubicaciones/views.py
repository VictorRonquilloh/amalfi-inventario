from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Urbanizacion, Manzana, Villa


@login_required
def lista_ubicaciones(request):
    urbanizaciones = Urbanizacion.objects.prefetch_related('manzanas__villas').all()
    return render(request, 'ubicaciones/lista_ubicaciones.html', {'urbanizaciones': urbanizaciones})
