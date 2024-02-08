from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import *
from .models import *

def index(request):
    return render(request,"producto/index.html")

#def producto_categoria_list(request):
   # objects = ProductoCategoria.objects.all()
   # context = {"objects_list":objects}
   # return render(request,"producto/producto_categoria_list.html", context)
   
class ProductoCategoriaList(ListView):
    model = ProductoCategoria
    # context_object_name = "object_list"
    # template_name = "producto/productocategoria_list.html"
    template_name = 'producto/producto_categoria_list.html'
    
    def get_queryset(self):
        if self.request.GET.get('consulta'):
           consultar = self.request.GET.get('consulta')
           object_list =ProductoCategoria.objects.filter(nombre__icontains=consultar)
        else:
           object_list = ProductoCategoria.objects.all()
           
        return object_list   
       
       
class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm 
    success_url = reverse_lazy('producto:productocategoria_list')                                                          
    template_name = 'producto/producto_categoria_create.html'    
    
    
# def productocategoria_detail(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/producto_categoria_detalles.html", {"object": consulta})
    
    
    
class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    template_name = 'producto/producto_categoria_detalles.html'                          
    context_object_name = 'categoria'
    