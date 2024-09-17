# produtos/models.py
from django.db import models


class Bolos(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome
    
class Destaques(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome


