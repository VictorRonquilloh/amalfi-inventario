from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Entrada, Salida
from .forms import EntradaForm, SalidaForm


@login_required
def lista_entradas(request):
    entradas = Entrada.objects.select_related('producto').all()
    return render(request, 'movimientos/lista_entradas.html', {'entradas': entradas})


@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.usuario = request.user
            entrada.save()
            messages.success(request, 'Entrada registrada correctamente.')
            return redirect('movimientos:lista_entradas')
    else:
        form = EntradaForm()
    return render(request, 'movimientos/form_entrada.html', {'form': form})
@login_required
def lista_salidas(request):
    salidas = Salida.objects.select_related('producto', 'villa').all()
    return render(request, 'movimientos/lista_salidas.html', {'salidas': salidas})


@login_required
def crear_salida(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST)
        if form.is_valid():
            salida = form.save(commit=False)
            salida.usuario = request.user
            salida.save()
            messages.success(request, 'Salida registrada correctamente.')
            return redirect('movimientos:lista_salidas')
    else:
        form = SalidaForm()
    return render(request, 'movimientos/form_salida.html', {'form': form})
