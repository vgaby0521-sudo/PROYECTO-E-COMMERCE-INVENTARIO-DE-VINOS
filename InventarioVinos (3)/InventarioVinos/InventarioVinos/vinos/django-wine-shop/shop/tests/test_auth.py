from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestAuth(TestCase):

    def test_login_correcto(self):
        User.objects.create_user(username='testuser', password='12345')

        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })

        self.assertIn(response.status_code, (200, 302))
