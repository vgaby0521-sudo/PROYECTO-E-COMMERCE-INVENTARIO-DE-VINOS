# 🍷 Wine Shop - Tienda de Vinos Online

Una tienda de vinos completa y profesional desarrollada con **Django**, **HTML puro**, **CSS personalizado** y **JavaScript vanilla**.

## 🎯 Características

✅ **Catálogo completo** - Visualización de productos con imágenes y detalles  
✅ **Carrito funcional** - Agregar, eliminar y actualizar cantidad de productos  
✅ **Sistema de autenticación** - Registro y login de usuarios  
✅ **Checkout seguro** - Proceso de compra en 3 pasos  
✅ **Panel de usuario** - Historial de pedidos, recompensas y notificaciones  
✅ **Panel de administrador** - Gestión completa del inventario (Django Admin)  
✅ **Sistema de recompensas** - Puntos por compra que se pueden canjear  
✅ **Diseño responsivo** - Compatible con desktop, tablet y móvil  
✅ **Paleta elegante** - Colores vino, burdeos, blanco y crema  

---

## 🚀 Instalación

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet (para imágenes de ejemplo)

### Paso 1: Clonar o descargar el proyecto

```bash
git clone <tu-repositorio>
cd wine-shop
```

O si descargaste un ZIP, extrae la carpeta y accede a ella.

### Paso 2: Crear un entorno virtual

```bash
python -m venv venv
```

**Activar el entorno:**

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Realizar migraciones

```bash
python manage.py migrate
```

### Paso 5: Crear superusuario (Administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla. Ejemplo:
- Username: `admin`
- Email: `admin@wineshop.com`
- Password: `Admin12345!`

### Paso 6: Poblar la base de datos con datos de prueba

```bash
python seed.py
```

Esto creará:
- 2 usuarios de prueba (admin y cliente)
- 5 categorías de vinos
- 3 proveedores
- 10 productos de ejemplo

### Paso 7: Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000**

---

## 👥 Usuarios de Prueba

Después de ejecutar el script `seed.py`, tendrás estos usuarios disponibles:

### Administrador
- **Usuario:** `admin`
- **Contraseña:** `Admin12345!`
- **Acceso:** Panel de administración en `/admin/`

### Cliente
- **Usuario:** `cliente1`
- **Contraseña:** `Cliente123!`
- **Acceso:** Tienda completa con compras

---

## 📂 Estructura del Proyecto

```
wine-shop/
├── wine_shop/              # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # Rutas principales
│   └── wsgi.py
├── shop/                   # Aplicación principal
│   ├── models.py          # Modelos de base de datos
│   ├── views.py           # Vistas y lógica
│   ├── urls.py            # Rutas de shop
│   ├── admin.py           # Configuración del admin
│   └── migrations/        # Migraciones de BD
├── templates/             # Templates HTML
│   ├── base.html          # Template base con CSS
│   ├── home.html
│   ├── catalogo.html
│   ├── detalle_producto.html
│   ├── carrito.html
│   ├── checkout.html
│   ├── login.html
│   ├── registro.html
│   ├── perfil_usuario.html
│   ├── mis_pedidos.html
│   └── detalle_pedido.html
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── media/                 # Imágenes de productos
├── manage.py             # Comando principal de Django
├── seed.py              # Script para poblar datos
├── requirements.txt     # Dependencias del proyecto
└── db.sqlite3          # Base de datos (se crea automáticamente)
```

---

## 🎨 Diseño y Paleta de Colores

- **Primario:** `#722f37` (Vino Burdeos)
- **Secundario:** `#8b4153` (Burdeos Oscuro)
- **Acento:** `#d4a574` (Dorado)
- **Fondo:** `#f5f1ed` (Crema)
- **Texto:** `#2c2c2c` (Gris Oscuro)

---

## 🔧 Comandos Útiles

### Crear migraciones
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Acceder al shell de Django
```bash
python manage.py shell
```

### Crear un nuevo superusuario
```bash
python manage.py createsuperuser
```

### Vaciar la base de datos (¡Cuidado!)
```bash
python manage.py flush
```

---

## 📄 Modelos de Base de Datos

### Usuarios y Perfil
- `User` - Usuario de Django
- `Perfil` - Perfil extendido con datos adicionales

### Productos
- `Categoria` - Categorías de vinos
- `Proveedor` - Proveedores de vinos
- `Producto` - Productos/Vinos disponibles

### Compras
- `CarritoItem` - Artículos en el carrito
- `Pedido` - Pedidos realizados
- `DetallePedido` - Detalles de cada producto en el pedido
- `Factura` - Facturas de pedidos

### Sistema
- `Inventario` - Movimientos de stock
- `Notificacion` - Notificaciones para usuarios
- `Recompensa` - Puntos de recompensa
- `SistemaPago` - Sistemas de pago configurados

---

## 🌐 Rutas Principales

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal (Home) |
| `/catalogo/` | Catálogo de productos |
| `/producto/<id>/` | Detalle de un producto |
| `/carrito/` | Carrito de compras |
| `/checkout/` | Proceso de compra |
| `/login/` | Iniciar sesión |
| `/registro/` | Crear nueva cuenta |
| `/perfil/` | Perfil del usuario |
| `/mis-pedidos/` | Historial de pedidos |
| `/admin/` | Panel de administrador |

---

## 💡 Características Técnicas

### Backend
- Django 4.2
- Base de datos SQLite (configurable a PostgreSQL)
- ORM de Django para modelos
- Sistema de autenticación integrado
- Admin personalizado

### Frontend
- HTML5 semántico
- CSS3 sin frameworks (sin Bootstrap ni Tailwind)
- JavaScript vanilla (sin jQuery ni React)
- Fetch API para comunicación con el servidor
- Diseño responsivo con media queries

### API
- Endpoints JSON para:
  - `/api/productos/` - Listado de productos
  - `/api/carrito/` - Estado del carrito
  - Gestión de carrito (agregar, eliminar, actualizar)
  - Crear pedidos

---

## 📱 Responsividad

El sitio está completamente optimizado para:
- **Desktop** - 1200px y superior
- **Tablet** - 768px a 1024px
- **Móvil** - 320px a 767px

---

## 🔐 Seguridad

✅ CSRF protection habilitada  
✅ Contraseñas hasheadas  
✅ Autenticación requerida para compras  
✅ Validación de datos en servidor y cliente  
✅ SQL Injection protegido (Django ORM)  

---


