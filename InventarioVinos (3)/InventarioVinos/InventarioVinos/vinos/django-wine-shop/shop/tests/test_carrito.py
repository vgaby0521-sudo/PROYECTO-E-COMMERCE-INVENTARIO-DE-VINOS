from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Producto, CarritoItem, Categoria, Proveedor


class TestCarrito(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='cliente', password='12345')

        categoria = Categoria.objects.create(nombre="Tintos", descripcion="", slug="tintos")
        proveedor = Proveedor.objects.create(nombre="Proveedor", correo="p@mail.com",
                                             telefono="123", direccion="Calle 1")

        self.producto = Producto.objects.create(
            nombre='Vino Tinto',
            descripcion='750ml',
            precio=35000,
            stock=10,
            categoria=categoria,
            proveedor=proveedor,
            imagen_url="https://img.com/x.jpg"
        )

        self.client.login(username='cliente', password='12345')

    def test_agregar_carrito(self):
        url = reverse('agregar_carrito', args=[self.producto.id])
        response = self.client.post(url, content_type="application/json", data='{}')
        self.assertIn(response.status_code, (200, 302))

    def test_modificar_cantidad_carrito(self):
        # Primero agregar
        self.client.post(reverse('agregar_carrito', args=[self.producto.id]),
                         content_type="application/json",
                         data='{}')

        item = CarritoItem.objects.get(usuario=self.user)

        url = reverse('actualizar_carrito', args=[item.id])
        response = self.client.post(url,
                                    content_type="application/json",
                                    data='{"cantidad":3}')
        self.assertIn(response.status_code, (200, 302))

    def test_eliminar_del_carrito(self):
        # Agregar para poder eliminar
        self.client.post(reverse('agregar_carrito', args=[self.producto.id]),
                         content_type="application/json",
                         data='{}')

        item = CarritoItem.objects.get(usuario=self.user)

        url = reverse('eliminar_carrito', args=[item.id])
        response = self.client.post(url, content_type="application/json", data='{}')
        self.assertIn(response.status_code, (200, 302))
