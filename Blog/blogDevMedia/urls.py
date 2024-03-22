from django.urls import path
from .views import postagem, postagem_list

urlpatterns = [
    path('', postagem, name='home' ),
    path('post/<int:id>', postagem_list, name='post' ),
]
