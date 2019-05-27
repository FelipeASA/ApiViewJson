from django.db import models

class productoModelo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    precio = models.IntegerField()
    fecha_ingreso = models.DateField()
    stock = models.IntegerField()

def __str__(self):
    return self.nombre+ ' ' +self.detalle+ ' ' +self.precio