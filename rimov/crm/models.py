from django.db import models
from rimov.core.models import Endereco


class Pessoa(Endereco):
    pass

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class PessoaFisica(Pessoa):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=True, blank=True)
    rg = models.CharField('RG', max_length=11, null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'pessoa física'
        verbose_name_plural = 'pessoas físicas'

    def __str__(self):
        return f'{self.nome} - {self.sobrenome}'


class PessoaJuridica(Pessoa):
    razao_social = models.CharField('razão social', max_length=100)
    nome_fantasia = models.CharField('nome fantasia', max_length=100, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=14, unique=True, null=True, blank=True)
    inscricao_estadual = models.CharField('inscrição estadual', max_length=25, null=True, blank=True)
    inscricao_municipal = models.CharField('inscrição municipal', max_length=25, null=True, blank=True)

    class Meta:
        ordering = ('razao_social',)
        verbose_name = 'pessoa jurídica'
        verbose_name_plural = 'pessoas jurídicas'

    def __str__(self):
        return self.razao_social
