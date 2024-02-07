from django import forms 
from. import models
from .models import Producto


class VendedorForm(forms.ModelForm): 
    class Meta: 
        model = models.Vendedor
        fields = "__all__"
                
class CompradorForm(forms.ModelForm):   
    class Meta: 
        model = models.Comprador
        fields = "__all__"
          

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['imagen', 'nombre', 'usado', 'descripcion', 'whatsapp']
      