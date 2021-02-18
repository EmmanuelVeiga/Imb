from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Cidade(models.Model):
    nome = models.CharField('cidade', max_length=100, unique=True)
    uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'


class Endereco(models.Model):
    endereco = models.CharField(
        'endereço',
        max_length=100,
        null=True,
        blank=True
    )
    numero = models.IntegerField('número', null=True, blank=True)
    complemento = models.CharField(
        'complemento',
        max_length=100,
        null=True,
        blank=True
    )
    bairro = models.CharField(
        'bairro',
        max_length=100,
        null=True,
        blank=True
    )
    cidade = models.ForeignKey(
        Cidade,
        verbose_name='cidade',
        on_delete=models.CASCADE,
    )
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True
