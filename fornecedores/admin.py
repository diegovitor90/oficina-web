from django.contrib import admin

from .models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'razao_social', 'cnpj', 'telefone', 'email', 'cidade', 'estado', 'ativo')
    search_fields = ('nome', 'razao_social', 'cnpj', 'telefone', 'email', 'cidade')
    list_filter = ('estado', 'ativo')
    ordering = ('nome',)
