from django.contrib import admin
from .models import Imovel


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'propriedade',
        'negocio',
        'categoria',
        'localizacao',
        'endereco',
        'area',
        'num_quarto',
        'num_banheiro',
        'num_vaga',
        'descricao',
        'corretor',
        'status'
    )
    list_display_links = ('titulo',)
    list_filter = ('status',)
    search_fields = ['titulo', 'corretor']
