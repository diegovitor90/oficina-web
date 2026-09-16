from django.test import TestCase
from django.urls import reverse

from .models import Veiculo


class VeiculoTestCase(TestCase):
	def setUp(self):
		self.payload = {
			'placa': 'ABC1D23',
			'marca': 'Toyota',
			'modelo': 'Corolla',
			'ano': 2022,
			'cor': 'Prata',
			'cliente': 'João da Silva',
			'ativo': True,
		}

	def test_cadastrar_veiculo_aparece_na_listagem(self):
		response = self.client.post(reverse('veiculos:cadastrar'), self.payload)

		self.assertEqual(response.status_code, 302)
		self.assertTrue(Veiculo.objects.filter(placa='ABC1D23').exists())
		lista_response = self.client.get(reverse('veiculos:lista'))
		self.assertContains(lista_response, 'ABC1D23')
		self.assertContains(lista_response, 'Corolla')

	def test_editar_veiculo_atualiza_dados(self):
		veiculo = Veiculo.objects.create(**self.payload)
		payload = {**self.payload, 'modelo': 'Yaris', 'cor': 'Branco'}

		response = self.client.post(
			reverse('veiculos:editar', args=[veiculo.pk]),
			payload,
		)

		self.assertEqual(response.status_code, 302)
		veiculo.refresh_from_db()
		self.assertEqual(veiculo.modelo, 'Yaris')
		self.assertEqual(veiculo.cor, 'Branco')

	def test_desativar_veiculo_altera_status(self):
		veiculo = Veiculo.objects.create(**self.payload)

		response = self.client.post(
			reverse('veiculos:desativar', args=[veiculo.pk]),
		)

		self.assertEqual(response.status_code, 302)
		veiculo.refresh_from_db()
		self.assertFalse(veiculo.ativo)
