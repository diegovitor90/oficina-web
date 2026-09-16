from django.contrib import admin

from .models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'duracao_minutos', 'ativo')
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo',)
    ordering = ('nome',)
