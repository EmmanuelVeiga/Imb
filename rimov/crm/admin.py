from django.contrib import admin
from .models import PessoaFisica, PessoaJuridica


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('nome', 'sobrenome')


@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('razao_social', 'nome_fantasia')
