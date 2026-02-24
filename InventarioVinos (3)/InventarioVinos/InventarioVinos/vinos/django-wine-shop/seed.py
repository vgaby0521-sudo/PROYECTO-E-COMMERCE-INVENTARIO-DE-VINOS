import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Categoria, Proveedor, Producto, Perfil

def crear_usuarios():
    print("Creando usuarios...")
    
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@wineshop.com',
            password='Admin12345!'
        )
        Perfil.objects.create(
            usuario=admin,
            nombre_completo='Administrador Wine Shop',
            tipo_usuario='admin',
            telefono='+1 (555) 123-4567'
        )
        print("✓ Usuario admin creado")
    
    if not User.objects.filter(username='cliente1').exists():
        cliente = User.objects.create_user(
            username='cliente1',
            email='cliente1@email.com',
            password='Cliente123!'
        )
        Perfil.objects.create(
            usuario=cliente,
            nombre_completo='Juan Carlos González',
            tipo_usuario='cliente',
            telefono='+1 (555) 987-6543',
            direccion='Calle Principal 123',
            ciudad='Madrid'
        )
        print("✓ Usuario cliente1 creado")

def crear_categorias():
    print("\nCreando categorías...")
    
    categorias_data = [
        {'nombre': 'Vinos Tintos', 'slug': 'vinos-tintos', 'descripcion': 'Vinos tintos de alta calidad'},
        {'nombre': 'Vinos Blancos', 'slug': 'vinos-blancos', 'descripcion': 'Vinos blancos refrescantes'},
        {'nombre': 'Vinos Rosados', 'slug': 'vinos-rosados', 'descripcion': 'Vinos rosados elegantes'},
        {'nombre': 'Espumantes', 'slug': 'espumantes', 'descripcion': 'Champagne y espumantes'},
        {'nombre': 'Licores', 'slug': 'licores', 'descripcion': 'Licores y destilados premium'},
    ]
    
    for cat_data in categorias_data:
        if not Categoria.objects.filter(slug=cat_data['slug']).exists():
            Categoria.objects.create(**cat_data)
            print(f"✓ Categoría '{cat_data['nombre']}' creada")

def crear_proveedores():
    print("\nCreando proveedores...")
    
    proveedores_data = [
        {
            'nombre': 'Bodega Española Premium',
            'correo': 'info@bodegaespañola.com',
            'telefono': '+34 923 123 456',
            'direccion': 'La Rioja, España'
        },
        {
            'nombre': 'Viñedos Franceses',
            'correo': 'contact@vignobles-fr.com',
            'telefono': '+33 3 80 22 34 56',
            'direccion': 'Burdeos, Francia'
        },
        {
            'nombre': 'Bodegas Argentinas',
            'correo': 'info@bodegasarg.com',
            'telefono': '+54 11 4555 6789',
            'direccion': 'Mendoza, Argentina'
        },
    ]
    
    for prov_data in proveedores_data:
        if not Proveedor.objects.filter(nombre=prov_data['nombre']).exists():
            Proveedor.objects.create(**prov_data)
            print(f"✓ Proveedor '{prov_data['nombre']}' creado")

def crear_productos():
    print("\nCreando productos...")

    productos_data = [
        {
            'nombre': 'Ribera del Duero Reserva 2018',
            'descripcion': 'Vino tinto de alta calidad con cuerpo y elegancia. Notas de frutas rojas y especias.',
            'precio': 25.99,
            'precio_oferta': 19.99,
            'stock': 50,
            'categoria_slug': 'vinos-tintos',
            'proveedor_nombre': 'Bodega Española Premium',
            'imagen_url': 'https://images.unsplash.com/photo-1510812431401-41d2cab2707d?w=500&h=500&fit=crop',
            'graduacion': '14.5',
            'pais': 'España',
            'vina': 'Bodegas de Ribera',
            'cosecha': 2018
        },
        {
            'nombre': 'Albariño Rías Baixas',
            'descripcion': 'Vino blanco fresco y aromático. Perfecto para mariscos y pescados.',
            'precio': 18.99,
            'stock': 60,
            'categoria_slug': 'vinos-blancos',
            'proveedor_nombre': 'Bodega Española Premium',
            'imagen_url': 'https://images.unsplash.com/photo-1586985289688-cacf0b2b4e2f?w=500&h=500&fit=crop',
            'graduacion': '12.5',
            'pais': 'España',
            'vina': 'Vinos de Galicia',
            'cosecha': 2022
        },
        {
            'nombre': 'Tempranillo Premium 2019',
            'descripcion': 'Vino tinto con sabores profundos de cereza y roble. Envejecido en barrica.',
            'precio': 22.50,
            'precio_oferta': 17.99,
            'stock': 40,
            'categoria_slug': 'vinos-tintos',
            'proveedor_nombre': 'Bodega Española Premium',
            'imagen_url': 'https://images.unsplash.com/photo-1509528214486-8d424e0c0bcd?w=500&h=500&fit=crop',
            'graduacion': '13.8',
            'pais': 'España',
            'vina': 'Tierras de Castilla',
            'cosecha': 2019
        },
        {
            'nombre': 'Rosado de Provence',
            'descripcion': 'Vino rosado delicado con aromas florales. Ideal para el verano.',
            'precio': 16.99,
            'stock': 45,
            'categoria_slug': 'vinos-rosados',
            'proveedor_nombre': 'Viñedos Franceses',
            'imagen_url': 'https://images.unsplash.com/photo-1594788318286-3d835c1cab83?w=500&h=500&fit=crop',
            'graduacion': '12.0',
            'pais': 'Francia',
            'vina': 'Vignobles de Provence',
            'cosecha': 2022
        },
        {
            'nombre': 'Champagne Brut Reserve',
            'descripcion': 'Champagne elegante y burbujeante. Ideal para celebraciones especiales.',
            'precio': 45.00,
            'precio_oferta': 35.99,
            'stock': 30,
            'categoria_slug': 'espumantes',
            'proveedor_nombre': 'Viñedos Franceses',
            'imagen_url': 'https://images.unsplash.com/photo-1608191078107-30f94e26ebf4?w=500&h=500&fit=crop',
            'graduacion': '12.5',
            'pais': 'Francia',
            'vina': 'Maison Champagne',
            'cosecha': 2019
        },
        {
            'nombre': 'Malbec Argentino Premium',
            'descripcion': 'Vino tinto robusto con sabores intensos de frutas negras y taninos suaves.',
            'precio': 28.99,
            'stock': 35,
            'categoria_slug': 'vinos-tintos',
            'proveedor_nombre': 'Bodegas Argentinas',
            'imagen_url': 'https://images.unsplash.com/photo-1510812431401-41d2cab2707d?w=500&h=500&fit=crop',
            'graduacion': '14.0',
            'pais': 'Argentina',
            'vina': 'Mendoza Wines',
            'cosecha': 2020
        },
        {
            'nombre': 'Torrontés Seco',
            'descripcion': 'Vino blanco argentino seco con notas cítricas y florales.',
            'precio': 17.50,
            'stock': 50,
            'categoria_slug': 'vinos-blancos',
            'proveedor_nombre': 'Bodegas Argentinas',
            'imagen_url': 'https://images.unsplash.com/photo-1586985289688-cacf0b2b4e2f?w=500&h=500&fit=crop',
            'graduacion': '12.8',
            'pais': 'Argentina',
            'vina': 'Bodegas de Salta',
            'cosecha': 2022
        },
        {
            'nombre': 'Cognac XO',
            'descripcion': 'Cognac extra old con sabores complejos y suavidad excepcional.',
            'precio': 85.00,
            'stock': 15,
            'categoria_slug': 'licores',
            'proveedor_nombre': 'Viñedos Franceses',
            'imagen_url': 'https://images.unsplash.com/photo-1569869118876-b53047fcc90a?w=500&h=500&fit=crop',
            'graduacion': '40.0',
            'pais': 'Francia',
            'vina': 'Maison Cognac',
            'cosecha': 1995
        },
        {
            'nombre': 'Vino Tinto Joven Tempranillo',
            'descripcion': 'Vino tinto joven de entrada, frutal y fácil de beber.',
            'precio': 12.99,
            'stock': 100,
            'categoria_slug': 'vinos-tintos',
            'proveedor_nombre': 'Bodega Española Premium',
            'imagen_url': 'https://images.unsplash.com/photo-1510812431401-41d2cab2707d?w=500&h=500&fit=crop',
            'graduacion': '13.0',
            'pais': 'España',
            'vina': 'Bodegas La Mancha',
            'cosecha': 2022
        },
        {
            'nombre': 'Sauvignon Blanc Francés',
            'descripcion': 'Vino blanco con carácter herbáceo y sabor cítrico refrescante.',
            'precio': 19.99,
            'stock': 55,
            'categoria_slug': 'vinos-blancos',
            'proveedor_nombre': 'Viñedos Franceses',
            'imagen_url': 'https://images.unsplash.com/photo-1586985289688-cacf0b2b4e2f?w=500&h=500&fit=crop',
            'graduacion': '12.5',
            'pais': 'Francia',
            'vina': 'Loire Valley',
            'cosecha': 2022
        },
    ]
    
    for prod_data in productos_data:
        if not Producto.objects.filter(nombre=prod_data['nombre']).exists():
            categoria = Categoria.objects.get(slug=prod_data.pop('categoria_slug'))
            proveedor = Proveedor.objects.get(nombre=prod_data.pop('proveedor_nombre'))
            imagen_url = prod_data.pop('imagen_url', 'https://via.placeholder.com/500')

            producto = Producto.objects.create(
                categoria=categoria,
                proveedor=proveedor,
                imagen_url=imagen_url,
                **prod_data
            )
            print(f"✓ Producto '{producto.nombre}' creado")

if __name__ == '__main__':
    print("=" * 50)
    print("Poblando base de datos de Wine Shop")
    print("=" * 50)
    
    crear_usuarios()
    crear_categorias()
    crear_proveedores()
    crear_productos()
    
    print("\n" + "=" * 50)
    print("✓ Base de datos poblada exitosamente!")
    print("=" * 50)
    print("\nUsuarios de prueba:")
    print("Admin: admin / Admin12345!")
    print("Cliente: cliente1 / Cliente123!")
