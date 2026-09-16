from django.db import models


class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=10, unique=True)
    marca = models.CharField('Marca', max_length=100, blank=True)
    modelo = models.CharField('Modelo', max_length=100, blank=True)
    ano = models.IntegerField('Ano', blank=True, null=True)
    cor = models.CharField('Cor', max_length=50, blank=True)
    cliente = models.CharField('Cliente', max_length=150, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['placa']

    def __str__(self):
        return f'{self.placa} - {self.modelo}'
