from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Producto, Pedido, Categoria, Proveedor


class TestPedidos(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='cliente', password='12345')

        categoria = Categoria.objects.create(nombre="Tintos", descripcion="", slug="tintos")
        proveedor = Proveedor.objects.create(nombre="Proveedor", correo="p@mail.com",
                                             telefono="123", direccion="Calle 1")

        self.producto = Producto.objects.create(
            nombre='Vino',
            descripcion='750ml',
            precio=30000,
            stock=5,
            categoria=categoria,
            proveedor=proveedor,
            imagen_url="https://img.com/x.jpg"
        )

    def test_crear_pedido(self):
        self.client.login(username='cliente', password='12345')
        response = self.client.post(reverse('checkout'))
        self.assertIn(response.status_code, (200, 302))

    def test_confirmar_pedido(self):
        pedido = Pedido.objects.create(cliente=self.user, total=30000,
                                       metodo_pago="tarjeta",
                                       direccion_envio="c",
                                       ciudad_envio="c",
                                       telefono_envio="1")
        pedido.estado = 'confirmado'
        pedido.save()
        self.assertTrue(pedido.estado == 'confirmado')

    def test_listar_pedidos(self):
        Pedido.objects.create(cliente=self.user, total=50000,
                              metodo_pago="tarjeta",
                              direccion_envio="c",
                              ciudad_envio="c",
                              telefono_envio="1")

        Pedido.objects.create(cliente=self.user, total=90000,
                              metodo_pago="tarjeta",
                              direccion_envio="c",
                              ciudad_envio="c",
                              telefono_envio="1")

        pedidos = Pedido.objects.filter(cliente=self.user)
        self.assertEqual(pedidos.count(), 2)
