from django.urls import path
from .views import *

urlpatterns = [
    path('veiculo/listar/<str:categoria>', listar_veiculo, name='listar_veiculo'),
    path('veiculo/perfil/<int:id>', perfil_veiculo, name='perfil_veiculo'),
    
]