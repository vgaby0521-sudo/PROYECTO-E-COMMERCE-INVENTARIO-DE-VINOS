from django.urls import reverse, resolve
from shop import views        # ← CORREGIDO
from django.test import TestCase

class TestUrls(TestCase):

    def test_url_home_resuelve(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
