from django.db import models


class Urbanizacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Manzana(models.Model):
    numero = models.CharField(max_length=10)
    urbanizacion = models.ForeignKey(Urbanizacion, on_delete=models.CASCADE, related_name='manzanas')

    def __str__(self):
        return f"Mz {self.numero} - {self.urbanizacion}"

    class Meta:
        unique_together = ('numero', 'urbanizacion')


class Villa(models.Model):
    numero = models.CharField(max_length=10)
    manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE, related_name='villas')

    def __str__(self):
        return f"Villa {self.numero} - {self.manzana}"

    class Meta:
        unique_together = ('numero', 'manzana')

