from django.db import models
from django.contrib.auth.models import User

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField(null=True, blank=True)  # nuevo
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # nuevo
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
