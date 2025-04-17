from django.test import TestCase
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='vinic', password='123456')

    def test_login_com_sucesso(self):
        response = self.client.post('/', {'username': 'vinic', 'password': '123456'})
        self.assertRedirects(response, '/home/')

    def test_login_com_erro(self):
        response = self.client.post('/', {'username': 'vinic', 'password': 'errado'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')  # garante que a tela de login reapareceu

    def test_protecao_da_home(self):
        response = self.client.get('/home/')
        self.assertRedirects(response, '/?next=/home/')  # redirecionado para login se não estiver logado
