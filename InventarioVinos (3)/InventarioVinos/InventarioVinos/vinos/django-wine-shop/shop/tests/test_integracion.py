from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Producto, Categoria, Proveedor


class TestIntegracion(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='cliente', password='12345')

        categoria = Categoria.objects.create(nombre="Tintos", descripcion="", slug="tintos")
        proveedor = Proveedor.objects.create(nombre="Proveedor", correo="p@mail.com",
                                             telefono="123", direccion="Calle 1")

        self.producto = Producto.objects.create(
            nombre='Vino Tinto', descripcion='750ml', precio=35000, stock=10,
            categoria=categoria, proveedor=proveedor, imagen_url="https://img.com/x.jpg"
        )

    def test_flujo_completo_compra(self):
        login = self.client.login(username='cliente', password='12345')
        self.assertTrue(login)

        # Agregar producto
        response = self.client.post(reverse('agregar_carrito', args=[self.producto.id]),
                                    content_type="application/json",
                                    data='{}')
        self.assertIn(response.status_code, (200, 302))

        # Ver carrito
        response = self.client.get(reverse('carrito'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.producto.nombre)

        # Checkout
        response = self.client.post(reverse('checkout'))
        self.assertIn(response.status_code, (200, 302))
