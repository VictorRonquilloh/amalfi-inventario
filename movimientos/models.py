from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Producto
from ubicaciones.models import Villa


class Entrada(models.Model):
    fecha = models.DateField()
    no_comprobante = models.CharField(max_length=50, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='entradas')
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Entrada {self.producto.codigo} - {self.cantidad} ({self.fecha})"

    class Meta:
        ordering = ['-fecha']


class Salida(models.Model):
    fecha = models.DateField()
    no_comprobante = models.CharField(max_length=50, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='salidas')
    cantidad = models.PositiveIntegerField()
    villa = models.ForeignKey(Villa, on_delete=models.PROTECT, related_name='salidas')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Salida {self.producto.codigo} - {self.cantidad} ({self.fecha})"

    @property
    def total_gastado(self):
        return self.cantidad * self.precio

    class Meta:
        ordering = ['-fecha']
