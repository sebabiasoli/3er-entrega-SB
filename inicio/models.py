from django.db import models

# Create your models here.

class Comprar(models.Model):
    articulo = models.CharField(max_length=30)
    precio = models.IntegerField()
    fecha_de_oferta = models.DateField(null=True)