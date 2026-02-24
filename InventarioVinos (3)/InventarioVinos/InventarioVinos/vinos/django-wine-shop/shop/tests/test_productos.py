from django.test import TestCase
from shop.models import Producto, Categoria, Proveedor


class TestProductos(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Tintos", descripcion="", slug="tintos")
        self.proveedor = Proveedor.objects.create(nombre="Proveedor", correo="p@mail.com",
                                                  telefono="123", direccion="Calle 1")

    def test_creacion_producto(self):
        producto = Producto.objects.create(
            nombre='Vino Tinto',
            descripcion='Botella de vino tinto chileno 750ml',
            precio=35000,
            stock=10,
            categoria=self.categoria,
            proveedor=self.proveedor,
            imagen_url="https://img.com/x.jpg"
        )
        self.assertEqual(producto.nombre, 'Vino Tinto')
        self.assertTrue(producto.stock > 0)
        self.assertIsNotNone(producto.id)

    def test_editar_producto(self):
        producto = Producto.objects.create(
            nombre='Vino Blanco',
            descripcion='Botella 750ml',
            precio=30000,
            stock=8,
            categoria=self.categoria,
            proveedor=self.proveedor,
            imagen_url="https://img.com/y.jpg"
        )
        producto.precio = 28000
        producto.save()
        self.assertEqual(producto.precio, 28000)

    def test_listar_productos(self):
        Producto.objects.create(nombre='A', descripcion='x', precio=10, stock=1,
                                categoria=self.categoria, proveedor=self.proveedor,
                                imagen_url="https://img.com/a.jpg")
        Producto.objects.create(nombre='B', descripcion='y', precio=20, stock=2,
                                categoria=self.categoria, proveedor=self.proveedor,
                                imagen_url="https://img.com/b.jpg")

        productos = Producto.objects.all()
        self.assertEqual(productos.count(), 2)

    def test_filtrar_productos_por_nombre(self):
        Producto.objects.create(nombre='Ron Medellín', descripcion='Añejo', precio=60000, stock=5,
                                categoria=self.categoria, proveedor=self.proveedor,
                                imagen_url="https://img.com/c.jpg")
        Producto.objects.create(nombre='Whisky', descripcion='12 años', precio=120000, stock=3,
                                categoria=self.categoria, proveedor=self.proveedor,
                                imagen_url="https://img.com/d.jpg")

        resultado = Producto.objects.filter(nombre__icontains="ron")
        self.assertEqual(resultado.count(), 1)
