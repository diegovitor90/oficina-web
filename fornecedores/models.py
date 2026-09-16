from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField('Nome', max_length=150)
    razao_social = models.CharField('Razão social', max_length=200, blank=True)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    email = models.EmailField('E-mail', blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    estado = models.CharField('UF', max_length=2, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
