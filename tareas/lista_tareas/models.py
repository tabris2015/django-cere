from django.db import models


# Create your models here.
class Tarea(models.Model):
    texto = models.CharField(max_length=300)
    prioridad = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField()
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    score = models.DecimalField(decimal_places=2, max_digits=6)
    