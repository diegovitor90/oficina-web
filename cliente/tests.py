from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class ClienteTestCase(TestCase):
    def setUp(self):
        self.payload = {
            'nome_completo': 'João da Silva',
            'tipo_pessoa': 'PF',
            'cpf_cnpj': '123.456.789-09',
            'telefone': '(11) 99999-1234',
            'whatsapp': '(11) 99999-1234',
            'email': 'joao@email.com',
            'cep': '01000-000',
            'endereco': 'Rua das Flores',
            'numero': '123',
            'complemento': 'Apto 1',
            'bairro': 'Centro',
            'cidade': 'São Paulo',
            'estado': 'SP',
            'observacoes': 'Cliente de teste',
            'ativo': True,
        }

    def test_cadastrar_cliente_aparece_na_listagem(self):
        response = self.client.post(reverse('clientes:cadastrar'), self.payload)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cliente.objects.filter(nome_completo='João da Silva').exists())

        lista_response = self.client.get(reverse('clientes:lista'))
        self.assertContains(lista_response, 'João da Silva')

    def test_editar_cliente_atualiza_dados(self):
        cliente = Cliente.objects.create(
            nome_completo='Maria Souza',
            tipo_pessoa='PF',
            cpf_cnpj='987.654.321-00',
            telefone='(21) 98888-0000',
            whatsapp='(21) 98888-0000',
            email='maria@email.com',
            cep='20000-000',
            endereco='Avenida Brasil',
            numero='10',
            bairro='Copacabana',
            cidade='Rio de Janeiro',
            estado='RJ',
            ativo=True,
        )

        payload = {
            **self.payload,
            'nome_completo': 'Maria Souza Silva',
            'telefone': '(21) 97777-1111',
            'email': 'maria.nova@email.com',
        }

        response = self.client.post(reverse('clientes:editar', args=[cliente.pk]), payload)

        self.assertEqual(response.status_code, 302)
        cliente.refresh_from_db()
        self.assertEqual(cliente.nome_completo, 'Maria Souza Silva')
        self.assertEqual(cliente.telefone, '(21) 97777-1111')
        self.assertEqual(cliente.email, 'maria.nova@email.com')

    def test_desativar_cliente_altera_status(self):
        cliente = Cliente.objects.create(
            nome_completo='Carlos Pereira',
            tipo_pessoa='PF',
            cpf_cnpj='111.222.333-44',
            telefone='(31) 98888-7777',
            whatsapp='(31) 98888-7777',
            email='carlos@email.com',
            ativo=True,
        )

        response = self.client.post(reverse('clientes:desativar', args=[cliente.pk]))

        self.assertEqual(response.status_code, 302)
        cliente.refresh_from_db()
        self.assertFalse(cliente.ativo)
