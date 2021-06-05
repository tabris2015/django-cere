from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30, default='normal')
    balance = models.IntegerField(default=0)
