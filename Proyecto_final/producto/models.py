from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProductoCategoria(models.Model):
    
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField(null=True, blank=True, verbose_name="descripción")
    
    def __str__(self)->str:
        
        return self.nombre
    class Meta:
        verbose_name="Categoría de producto"
        verbose_name_plural="Categorías de productos"
        
        
class Producto(models.Model): 
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, on_delete=models.SET_NULL)
    nombre=models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    cantidad=models.FloatField()
    precio=models.FloatField()
    descripcion=models.TextField(null = True, blank = True, verbose_name="descripción")
    fecha_de_actualizacion=models.DateTimeField(null=True, blank=True, default=timezone.now, editable=False) 
    
    
    def __str__(self)->str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}" 
           
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
