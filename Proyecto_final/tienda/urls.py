from django.urls import path
from django.contrib.auth import views as auth_views
from tienda import views
from .views import about, crear_producto


urlpatterns = [
   
    path('',views.index,name ="index"),
    
    path('vendedor/list',views.vendedor_list,name='vendedor_list'),
    
    path('vendedor/creat',views.vendedor_creat,name='vendedor_creat'),
    
    path('eliminarVendedor/<vendedor_nombre>',views.eliminar_vendedor,name='EliminarVendedor'),
    
    
    
    path('comprador/list',views.comprador_list,name='comprador_list'),
    
    path('comprador/creat',views.comprador_creat,name='comprador_creat'),
    
    path('eliminarComprador/<comprador_nombre>',views.eliminar_comprador,name='EliminarComprador'),
    
    #login
    
    path('login/', views.login_request, name='Login'),
    
    path('registro/', views.registro, name='Registro'),
    
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('about',about,name="about"),
    
    #crear producto
    
    path('crear_producto/',views.crear_producto,name="crear_producto"),
   
]