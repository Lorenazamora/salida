from django.urls import path
from.views import *


urlpatterns = [
    path('lista_producto/', vista_lista_Producto, name='vista_lista_producto'),
    path('lista_marca/', vista_lista_Marca, name='vista_lista_marca'), 
    path('lista_categoria/', vista_lista_Categoria, name='vista_lista_categoria'),
    path('agregar_producto/', vista_agregar_producto, name='vista_agregar_producto'), 
    path('ver_producto/<int:id_prod>/',vista_ver_producto, name='vista_ver_producto'), 
    path('editar_producto/<int:id_prod>/',vista_editar_producto, name='vista_editar_producto'), 
    path('eliminar_producto/<int:id_prod>/',vista_eliminar_producto, name='vista_eliminar_producto'), 
    path('login/', vista_login, name='vista_login'),
    path('logout/', vista_logout, name='vista_logout'),
    path('registrar/', vista_registrar, name='vista_registrar'),
    path('ws/productos/', ws_productos_vista, name = 'ws_productos_vista'),


]