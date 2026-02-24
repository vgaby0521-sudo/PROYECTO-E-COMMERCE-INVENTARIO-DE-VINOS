from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestUsuarios(TestCase):

    # Registro
    def test_registro_usuario(self):
        response = self.client.post(reverse('registro'), {
            'username': 'nuevo',
            'password1': 'abcd1234',
            'password2': 'abcd1234'
        })
        self.assertIn(response.status_code, (200, 302))

    # Login
    def test_login_correcto(self):
        User.objects.create_user(username='testuser', password='12345')

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertIn(response.status_code, (200, 302))

    # Roles
    def test_roles_usuario(self):
        user = User.objects.create_user(username='admin', password='12345', is_staff=True)
        self.assertTrue(user.is_staff)
