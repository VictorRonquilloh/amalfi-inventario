from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"


class Producto(models.Model):
    UNIDAD_CHOICES = [
        ('Unidad', 'Unidad'),
        ('Saco', 'Saco'),
        ('m3', 'Metro cúbico'),
        ('m2', 'Metro cuadrado'),
        ('m', 'Metro'),
        ('kg', 'Kilogramo'),
        ('Galon', 'Galón'),
        ('Litro', 'Litro'),
        ('Caneca', 'Caneca'),
        ('Caja', 'Caja'),
        ('Global', 'Global'),
        ('Rollo', 'Rollo'),
        ('Viaje', 'Viaje'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.CharField(max_length=255)
    unidad = models.CharField(max_length=20, choices=UNIDAD_CHOICES, default='Unidad')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

    @property
    def existencia(self):
        total_entradas = sum(e.cantidad for e in self.entradas.all())
        total_salidas = sum(s.cantidad for s in self.salidas.all())
        return total_entradas - total_salidas
