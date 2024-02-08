from django.urls import path

from .import views

app_name = "producto"

urlpatterns = [
   
    path('',views.index,name ="index"),
    
    #path('producto_categoria/list',views.producto_categoria_list,name ="producto_categoria_list"),
 
    path('productocategoria/list/',views.ProductoCategoriaList.as_view(),name ="productocategoria_list"),#las classes no se ejecutan de forma automatica  asi que agregamso el.as_view()
    
    path('productocategoria/create/', views.ProductoCategoriaCreate.as_view(), name="producto_categoria_create"),
    
     path('producto_categoria/detalles/<int:pk>/', views.ProductoCategoriaDetail.as_view(), name="producto_categoria_detalles"),


]     