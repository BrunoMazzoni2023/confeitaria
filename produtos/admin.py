from django.contrib import admin
from .models import Bolos, Destaques

class BolosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'imagem')
    search_fields = ('nome',)
    list_filter = ('nome',)

class DestaquesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'imagem')
    search_fields = ('nome',)
    list_filter = ('nome',)

admin.site.register(Bolos, BolosAdmin)
admin.site.register(Destaques, DestaquesAdmin)
