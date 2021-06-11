from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Encargado(models.Model):
    CARRERA_CHOICES = [
        ('ETN', 'Electrónica'),
        ('MEC', 'Mecánica'),
        ('TEL', 'Telecomunicaciones'),
    ]
    nombre = models.CharField(max_length=200)
    carrera = models.CharField(max_length=3, choices=CARRERA_CHOICES, default='ETN')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Item(models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    encargado = models.ForeignKey(Encargado, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.marca}:{self.nombre}'
