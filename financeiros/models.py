from django.db import models


class Financeiro(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    descricao = models.CharField('Descrição', max_length=200)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    data = models.DateField('Data', auto_now_add=True)
    observacao = models.TextField('Observação', blank=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.descricao
