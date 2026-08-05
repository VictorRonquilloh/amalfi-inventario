from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Producto, Categoria


@login_required
def lista_productos(request):
    productos = Producto.objects.select_related('categoria').all().order_by('descripcion')

    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')

    if query:
        productos = productos.filter(
            Q(codigo__icontains=query) | Q(descripcion__icontains=query)
        )

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()

    return render(request, 'catalogo/lista_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'query': query or '',
        'categoria_id': categoria_id or '',
    })