from django.contrib import admin

from .models import Financeiro


@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo', 'valor', 'data', 'observacao')
    search_fields = ('descricao', 'observacao')
    list_filter = ('tipo', 'data')
    ordering = ('-data',)
