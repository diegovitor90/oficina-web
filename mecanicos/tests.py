from django.test import TestCase

from django.urls import reverse

from .models import Mecanico


class MecanicoTestCase(TestCase):
	def setUp(self):
		self.payload = {
			'nome': 'Carlos Oliveira',
			'cpf': '123.456.789-00',
			'telefone': '(61) 3333-4444',
			'whatsapp': '(61) 99999-8888',
			'especialidade': 'Motor e injeção eletrônica',
			'data_admissao': '2024-02-15',
			'ativo': True,
		}

	def test_cadastrar_mecanico_aparece_na_listagem(self):
		response = self.client.post(reverse('mecanicos:cadastrar'), self.payload)

		self.assertEqual(response.status_code, 302)
		mecanico = Mecanico.objects.get(nome='Carlos Oliveira')
		self.assertEqual(mecanico.especialidade, 'Motor e injeção eletrônica')
		self.assertEqual(str(mecanico.data_admissao), '2024-02-15')

		lista_response = self.client.get(reverse('mecanicos:lista'))
		self.assertEqual(lista_response.status_code, 200)
		self.assertContains(lista_response, 'Carlos Oliveira')

	def test_editar_mecanico_atualiza_dados(self):
		mecanico = Mecanico.objects.create(**self.payload)
		payload = {
			**self.payload,
			'nome': 'Carlos Oliveira Silva',
			'telefone': '(61) 98888-7777',
			'especialidade': 'Suspensão e freios',
		}

		response = self.client.post(
			reverse('mecanicos:editar', args=[mecanico.pk]),
			payload,
		)

		self.assertEqual(response.status_code, 302)
		mecanico.refresh_from_db()
		self.assertEqual(mecanico.nome, 'Carlos Oliveira Silva')
		self.assertEqual(mecanico.telefone, '(61) 98888-7777')
		self.assertEqual(mecanico.especialidade, 'Suspensão e freios')

	def test_desativar_mecanico_altera_status(self):
		mecanico = Mecanico.objects.create(**self.payload)

		response = self.client.post(
			reverse('mecanicos:desativar', args=[mecanico.pk]),
		)

		self.assertEqual(response.status_code, 302)
		mecanico.refresh_from_db()
		self.assertFalse(mecanico.ativo)
