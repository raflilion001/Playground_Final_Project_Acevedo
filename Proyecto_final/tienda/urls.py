from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.index,name ="index"),
    
    path('vendedor/list',views.vendedor_list,name='vendedor_list'),
    
    path('vendedor/creat',views.vendedor_creat,name='vendedor_creat'),
    
    path('eliminarVendedor/<vendedor_nombre>',views.eliminar_vendedor,name='EliminarVendedor'),
    
    path('comprador/list',views.comprador_list,name='comprador_list'),
    
    path('comprador/creat',views.comprador_creat,name='comprador_creat'),
    
    path('eliminarComprador/<comprador_nombre>',views.eliminar_comprador,name='EliminarComprador'),
    

]