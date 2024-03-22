from django.urls import path
from .views import *

urlpatterns = [
    path('marca/cadastrar/', cadastrar_marca, name='cadastrar_marca'),
    path('marca/listar/', listar_marca, name='listar_marca'),
    path('marca/editar/<int:id>', editar_marca, name='editar_marca'),
    path('marca/produto/<int:id>', listar_produtos_marca, name='marca_produto'),
    path('marca/remover/<int:id>', remover_marca, name='remover_marca'),

    path('produto/cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('produto/listar/', listar_produto, name='listar_produto'),
    path('produto/editar/<int:id>', editar_produto, name='editar_produto'),
    path('produto/remover/<int:id>', remover_produto, name='remover_produto'),
    path('produto/perfil/<int:id>', perfil_produto, name='perfil_produto'),

    path('categoria/cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    path('categoria/listar/', listar_categoria, name='listar_categoria'),
    path('categoria/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categoria/remover/<int:id>', remover_categoria, name='remover_categoria'),
    path('categoria/produto/<int:id>', listar_produtos_categoria, name='categoria_produto'),
]