from django.db import models


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
    cep = models.CharField('CEP', max_length=9, null=True, blank=True)

    class Meta:
        abstract = True
