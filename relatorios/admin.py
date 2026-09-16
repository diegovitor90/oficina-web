from django.contrib import admin

from .models import Relatorio


@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'descricao', 'data_geracao', 'arquivo')
    search_fields = ('titulo', 'tipo', 'descricao')
    list_filter = ('tipo',)
    ordering = ('-data_geracao',)
