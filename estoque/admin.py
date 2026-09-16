from django.contrib import admin

from .models import ItemEstoque


@admin.register(ItemEstoque)
class ItemEstoqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'quantidade', 'preco_unitario', 'categoria', 'fornecedor', 'ativo')
    search_fields = ('nome', 'codigo', 'categoria', 'fornecedor')
    list_filter = ('categoria', 'ativo')
    ordering = ('nome',)
