from django import forms 

from. import models

class VendedorForm(forms.ModelForm): 
    class Meta: 
        model = models.Vendedor
        fields = "__all__"
                
class CompradorForm(forms.ModelForm):   
    class Meta: 
        model = models.Comprador
        fields = "__all__"