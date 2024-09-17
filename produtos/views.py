# produtos/views.py
from django.shortcuts import render, get_object_or_404
from .models import Bolos, Destaques

def index(request):
    destaques = Destaques.objects.all()  # Obtendo todos os destaques
    return render(request, 'index.html', {'destaques': destaques})

def teste(request):
    return render(request, 'teste.html')

def teste2(request):
    return render(request, 'teste2.html')

def bolos_list(request):
    bolos = Bolos.objects.all()
    return render(request, 'bolos_list.html', {'bolos': bolos})

def bolo_detalhes(request, id):
    bolo = get_object_or_404(Bolos, id=id)
    return render(request, 'bolo_detalhes.html', {'bolo': bolo})

def destaques(request):
    destaques = Destaques.objects.all()
    return render(request, 'destaques.html', {'destaques': destaques})