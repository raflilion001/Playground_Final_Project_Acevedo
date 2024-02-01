from django.db import models

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30 )
    apellido= models.CharField(max_length= 50)
    email= models.EmailField()
      
    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido},{self.email}"
    
    
class Comprador(models.Model):
    nombre= models.CharField(max_length=30 )
    apellido= models.CharField(max_length= 50)
    email= models.EmailField()
      
    def __str__(self) -> str:
        return f"{self.nombre},{self.apellido},{self.email}"
    
    
    