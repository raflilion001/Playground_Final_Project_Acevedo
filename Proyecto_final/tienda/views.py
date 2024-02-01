from django.shortcuts import render,redirect, get_object_or_404

from . import models,forms 



def index(request):
     return render(request,"tienda/index.html")

def vendedor_list(request):
    consulta = models.Vendedor.objects.all() 
    contexto = {"vendedor": consulta} 
    return render (request, "tienda/vendedor_list.html", contexto) 


def vendedor_creat(request):
    if request.method =="POST":
        form =forms.VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendedor_list")
    else:
        form= forms.VendedorForm()    
    return render(request,"tienda/vendedor_creat.html",{"form":form})


def eliminar_vendedor(request,vendedor_nombre):
    vendedor = models.Vendedor.objects.get(nombre=vendedor_nombre)
    vendedor.delete()
    
    vendedores =models.Vendedor.objects.all() 
    contexto = {"vendedores":vendedores}
    return render (request, "tienda/vendedor_list.html",contexto)


#####################################

def comprador_list(request):
    consulta = models.Comprador.objects.all() 
    contexto = {"comprador": consulta} 
    return render (request, "tienda/comprador_list.html", contexto) 

def comprador_creat(request):
    if request.method =="POST":
        form =forms.CompradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comprador_list")
    else:
        form= forms.CompradorForm()    
    return render(request,"tienda/comprador_creat.html",{"form":form})

def eliminar_comprador(request,comprador_nombre):
    comprador = models.Comprador.objects.get(nombre=comprador_nombre)
    comprador.delete()
    
    compradores =models.Comprador.objects.all() 
    contexto = {"compradores":compradores}
    return render (request, "tienda/comprador_list.html",contexto)
