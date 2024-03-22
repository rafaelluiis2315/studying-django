
from django.urls import path
from .views import *
urlpatterns = [
    path('listar_usuario/', listar_usuario, name='listar_usuario'),
    path('registrar_usuario/', reguistrar_usuario, name='registrar_usuario'),
    path('logar/', logar, name='logar'),
    path('remover_usuario/<int:id>', remover_usuario, name='remover_usuario'),
    path('deslogar/', deslogar, name='deslogar')
]