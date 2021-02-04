from django.contrib import admin
from .models import Imovel, Galeria


class GaleriaInline(admin.TabularInline):
    model = Galeria
    extra = 0


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    inlines = (GaleriaInline,)
    list_display = (
        'id',
        'titulo',
        'propriedade',
        'negocio',
        'categoria',
        'valor',
        'localizacao',
        'endereco',
        'area',
        'num_quarto',
        'num_banheiro',
        'num_vaga',
        'descricao',
        'corretor',
        'status',
        'video'
    )
    list_display_links = ('titulo',)
    list_filter = ('status',)
    search_fields = ['titulo', 'corretor']
