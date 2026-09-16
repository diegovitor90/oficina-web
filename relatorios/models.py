from django.db import models


class Relatorio(models.Model):
    titulo = models.CharField('Título', max_length=200)
    tipo = models.CharField('Tipo', max_length=100, blank=True)
    descricao = models.TextField('Descrição', blank=True)
    data_geracao = models.DateTimeField('Data de geração', auto_now_add=True)
    arquivo = models.FileField('Arquivo', upload_to='relatorios/', blank=True, null=True)

    class Meta:
        ordering = ['-data_geracao']

    def __str__(self):
        return self.titulo
