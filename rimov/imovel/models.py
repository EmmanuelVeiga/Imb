import uuid
import os

from django.db import models
from django.conf import settings


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("imoveis", filename)


STATUS = (
    ("Disponível", "Disponível"),
    ("Indisponível", "Indisponível")

)
TIPO_PROPRIEDADE = (
    ("Apartamento", "Apartamento"),
    ("Casa", "Casa"),
    ("Casa Condomínio", "Casa Condomínio"),
    ("Casa Vila", "Casa Vila"),
    ("Cobertura", "Cobertura"),
    ("Comercial", "Comercial"),
    ("Fazenda", "Fazenda"),
    ("Flat", "Flat"),
    ("Kitnet", "Kitnet"),
    ("Loft", "Loft"),
    ("Sobrado", "Sobrado"),
    ("Terreno", "Terreno Padrão"),

)

CATEGORIA = (
    ("Alto Padrão", "Alto Padrão"),
    ("Médio Padrão", "Médio Padrão"),
    ("Baixo Padrão", "Baixo Padrão")

)

NEGOCIO = (
    ("Aluguel", "Aluguel"),
    ("Arrendamento", "Arrendamento"),
    ("Em Construção", "Em Construção"),
    ("Venda", "Venda")

)


class Imovel(models.Model):
    titulo = models.CharField(max_length=250,)
    propriedade = models.TextField(choices=TIPO_PROPRIEDADE)
    negocio = models.TextField(choices=NEGOCIO)
    categoria = models.TextField(choices=CATEGORIA)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default='some_value', blank=True)
    localizacao = models.CharField(max_length=300, blank=True)
    endereco = models.CharField(max_length=300, blank=True)
    area = models.IntegerField(null=True, blank=True)
    num_quarto = models.IntegerField(null=True, blank=True)
    num_banheiro = models.IntegerField(null=True, blank=True)
    num_vaga = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(unique=True, blank=True)
    corretor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    status = models.TextField(choices=STATUS)
    video = models.CharField(max_length=3000, default='', blank=True)

    def imagens_url(self):
        if self.imagens and hasattr(self.imagens, 'url'):
            return self.imagens.url

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
        ordering = ['-pk']

    def __str__(self):
        return self.titulo

    def first_image(self):
        if self.imagem_imoveis:
            return self.imagem_imoveis.first()


class Galeria(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='imagem_imoveis', null=True)
    imagem = models.FileField('Imagem', upload_to=get_file_path, blank=False, null=True)

    class Meta:
        verbose_name = "Galeria do Imóvel"
        verbose_name_plural = "Galeria do Imóvel"
