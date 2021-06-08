from django.db import models


# Create your models here.
class Tarea(models.Model):
    texto = models.CharField(max_length=300)
    prioridad = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField()
