from django.db import models


class ItemEstoque(models.Model):
    nome = models.CharField('Nome do item', max_length=150)
    codigo = models.CharField('Código', max_length=50, unique=True, blank=True)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco_unitario = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2, default=0)
    categoria = models.CharField('Categoria', max_length=100, blank=True)
    fornecedor = models.CharField('Fornecedor', max_length=150, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
