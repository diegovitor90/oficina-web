from django.db import models


class Servico(models.Model):
    nome = models.CharField('Nome do serviço', max_length=150)
    descricao = models.TextField('Descrição', blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    duracao_minutos = models.IntegerField('Duração (minutos)', default=0)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
