from django.test import TestCase
from django.urls import reverse
from shop.models import Producto, Categoria


class TestViews(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="General")
        self.producto = Producto.objects.create(
            nombre='Vino Tinto',
            descripcion='750ml',
            precio=35000,
            stock=10,
            categoria=self.categoria
        )

    def test_detalle_producto(self):
        response = self.client.get(reverse('detalle_producto', args=[self.producto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.producto.nombre)
