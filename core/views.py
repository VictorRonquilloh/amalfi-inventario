from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogo.models import Producto
from movimientos.models import Entrada, Salida


@login_required
def dashboard(request):
    productos = Producto.objects.select_related('categoria').all()

    total_productos = productos.count()
    stock_bajo = [p for p in productos if p.existencia <= 5]

    ultimas_entradas = Entrada.objects.select_related('producto').all()[:5]
    ultimas_salidas = Salida.objects.select_related('producto', 'villa').all()[:5]

    total_gastado = sum(s.total_gastado for s in Salida.objects.all())

    context = {
        'total_productos': total_productos,
        'stock_bajo': stock_bajo,
        'ultimas_entradas': ultimas_entradas,
        'ultimas_salidas': ultimas_salidas,
        'total_gastado': total_gastado,
    }
    return render(request, 'core/dashboard.html', context)
