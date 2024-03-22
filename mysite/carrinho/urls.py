from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:brand_id>/', views.detail_brand , name= 'detail_brand')
]