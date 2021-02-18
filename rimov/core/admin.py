from django.contrib import admin
from .models import Cidade


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('nome',)
