from django.shortcuts import render,redirect, get_object_or_404

from . import models,forms 

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm


def index(request):
     return render(request,"tienda/index.html")

def vendedor_list(request):
    consulta = models.Vendedor.objects.all() 
    contexto = {"vendedores": consulta} 
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
    contexto = {"compradores": consulta} 
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


class CustomLoginView(LoginView):
    template_name = 'tu_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'tu_app/logout.html'
    
    
    
    
#login

def login_request(request):
    if request.method == "POST":   
            
        form= AuthenticationForm(request,data=request.POST)  
        if form.is_valid():   #Si paso la verificacion  
              
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password") 
            
            user = authenticate(username=usuario, password=contraseña)
            
            login(request, user) 
            
            return render (request, "tienda/index.html",{"mensaje":f'Bienvenido de nuevo {user.username}'})  # type: ignore
    else:
        form=AuthenticationForm()             
    return render(request,"tienda/login.html",{"form":form})


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Accede al nombre de usuario correctamente
            form.save()
            return render(request, "tienda/index.html", {"mensaje": "Usuario creado: "})
    else:
        form = UserCreationForm()
    return render(request, "tienda/registro.html", {"form": form})



#  crear lista de about.html
def about(request):
    return render(request,"tienda/about.html")
    



# crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # Asignar el usuario actual al producto
            producto.save()
            return redirect('tienda/index.html')  # Redirigir a la lista de productos después de guardar
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

 #   edicion de productos
 
 
def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'modificar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')