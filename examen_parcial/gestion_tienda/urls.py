from django.urls import path
from . import views

app_name = 'gestion_tienda'

urlpatterns = [
    path('',views.index, name='index'),
    path ('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
    path('panelNavegacion', views.panelNavegacion, name='panelNavegacion'),
    path('eliminarUsuario/<str:ind>',views.eliminarUsuario,name='eliminarUsuario'),
    path ('datosProducto', views.datosProducto, name='datosProducto'),
    path ('eliminarProducto/<str:ind>',views.eliminarProducto,name='eliminarProducto'),
]
