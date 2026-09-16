from django.contrib import admin

from .models import OrdemServico


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cliente', 'veiculo', 'servico', 'status', 'valor_total', 'data_abertura')
    search_fields = ('codigo', 'cliente', 'veiculo', 'servico')
    list_filter = ('status',)
    ordering = ('-data_abertura',)
