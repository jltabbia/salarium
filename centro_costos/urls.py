from django.urls import path, re_path
from .views import CentroCostosHomeView, AgregarCentroCosto, editarCentroCosto, eliminarCentroCosto

app_name='centro_costos'

urlpatterns = [
    path('', CentroCostosHomeView, name='index'),
    path('agregar',AgregarCentroCosto.as_view(),name="agregar"),
    path('eliminar', eliminarCentroCosto, name='eliminar'),
    path('editar', editarCentroCosto, name='editar'),
    
]