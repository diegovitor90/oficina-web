from django.test import TestCase


class PecaTestCase(TestCase):
    def test_exemplo(self):
        self.assertEqual(1 + 1, 2)
