from django.contrib import admin

from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'cor', 'cliente', 'ativo')
    search_fields = ('placa', 'marca', 'modelo', 'cliente')
    list_filter = ('marca', 'ativo')
    ordering = ('placa',)
