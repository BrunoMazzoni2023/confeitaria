# produtos/urls.py

from django.urls import path
from .views import index, bolos_list, bolo_detalhes, teste, teste2, destaques

urlpatterns = [
    path('', index, name='index'),
    path('bolos/', bolos_list, name='bolos_list'),
    path('bolos/<int:id>/', bolo_detalhes, name='bolo_detalhes'),
    path('teste/', teste, name='teste'),
    path('teste2/', teste2, name='teste2'),
    path('destaques/<int:id>/', destaques, name='destaques'),


]
