from django import forms 
from. import models
from .models import Producto
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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
        

class CustomCreationForm(UserCreationForm):
    class Meta : 
        model = User
        fields = ['username', 'password1', 'password2']  
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "password1": forms.PasswordInput(attrs={"class":"form-control"}),
            "password2": forms.PasswordInput(attrs={"class":"form-control"}),
        }      
      