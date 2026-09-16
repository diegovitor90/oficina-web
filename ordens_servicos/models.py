from django.db import models


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    codigo = models.CharField('Código', max_length=50, unique=True)
    cliente = models.CharField('Cliente', max_length=150)
    veiculo = models.CharField('Veículo', max_length=150, blank=True)
    servico = models.CharField('Serviço', max_length=150, blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='aberta')
    valor_total = models.DecimalField('Valor total', max_digits=10, decimal_places=2, default=0)
    data_abertura = models.DateTimeField('Data de abertura', auto_now_add=True)
    atualizado_em = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        ordering = ['-data_abertura']

    def __str__(self):
        return f'{self.codigo} - {self.cliente}'
