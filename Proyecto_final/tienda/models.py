from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido},{self.email}"

class Comprador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido},{self.email}"

class Producto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    usado = models.BooleanField()
    descripcion = models.TextField()
    whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre