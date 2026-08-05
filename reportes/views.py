from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from catalogo.models import Producto
from movimientos.models import Entrada, Salida
from ubicaciones.models import Manzana, Villa


@login_required
def reporte_por_villa(request):
    villas = Villa.objects.select_related('manzana', 'manzana__urbanizacion').all()
    data = []
    for villa in villas:
        salidas = Salida.objects.filter(villa=villa)
        total = sum(s.total_gastado for s in salidas)
        if total > 0:
            data.append({'villa': villa, 'total': total, 'movimientos': salidas.count()})
    data.sort(key=lambda x: x['total'], reverse=True)
    return render(request, 'reportes/por_villa.html', {'data': data})


@login_required
def reporte_por_manzana(request):
    manzanas = Manzana.objects.select_related('urbanizacion').all()
    data = []
    for manzana in manzanas:
        salidas = Salida.objects.filter(villa__manzana=manzana)
        total = sum(s.total_gastado for s in salidas)
        if total > 0:
            data.append({'manzana': manzana, 'total': total, 'movimientos': salidas.count()})
    data.sort(key=lambda x: x['total'], reverse=True)
    return render(request, 'reportes/por_manzana.html', {'data': data})


@login_required
def kardex_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    entradas = producto.entradas.all()
    salidas = producto.salidas.all()

    movimientos = []
    for e in entradas:
        movimientos.append({'fecha': e.fecha, 'tipo': 'Entrada', 'cantidad': e.cantidad, 'ref': e.no_comprobante})
    for s in salidas:
        movimientos.append({'fecha': s.fecha, 'tipo': 'Salida', 'cantidad': -s.cantidad, 'ref': f'Villa {s.villa}'})
    movimientos.sort(key=lambda x: x['fecha'])

    saldo = 0
    for m in movimientos:
        saldo += m['cantidad']
        m['saldo'] = saldo

    return render(request, 'reportes/kardex.html', {'producto': producto, 'movimientos': movimientos})


@login_required
def lista_kardex(request):
    productos = Producto.objects.all().order_by('descripcion')
    return render(request, 'reportes/lista_kardex.html', {'productos': productos})

from ubicaciones.models import Villa

@login_required
def lista_kardex_villas(request):
    villas = Villa.objects.select_related('manzana', 'manzana__urbanizacion').all()
    return render(request, 'reportes/lista_kardex_villas.html', {'villas': villas})


@login_required
def kardex_villa(request, villa_id):
    villa = Villa.objects.select_related('manzana', 'manzana__urbanizacion').get(id=villa_id)
    salidas = Salida.objects.filter(villa=villa).select_related('producto').order_by('fecha')

    total = sum(s.total_gastado for s in salidas)

    return render(request, 'reportes/kardex_villa.html', {
        'villa': villa,
        'salidas': salidas,
        'total': total,
    })
