# 🧪 Guía para Ejecutar Pruebas Funcionales - Wine Shop

## 📋 Pre-requisitos

Antes de ejecutar las pruebas funcionales, asegúrate de tener:

1. **Python 3.8+** instalado
2. **Google Chrome** instalado (última versión)
3. **Proyecto Wine Shop** funcionando correctamente

## 🚀 Instalación de Dependencias

### Paso 1: Activar el entorno virtual

**Windows:**
```bash
cd InventarioVinos\vinos\django-wine-shop
env\Scripts\activate
```

**macOS/Linux:**
```bash
cd InventarioVinos/vinos/django-wine-shop
source env/bin/activate
```

### Paso 2: Instalar dependencias para pruebas

```bash
pip install selenium==4.37.0
pip install webdriver-manager==4.0.2
pip install openpyxl==3.1.5
```

O instalar todas a la vez:
```bash
pip install selenium webdriver-manager openpyxl
```

## 🏃 Ejecutar el Proyecto

**IMPORTANTE:** El proyecto debe estar corriendo ANTES de ejecutar las pruebas.

### Paso 1: Iniciar el servidor Django

En una terminal:

```bash
cd InventarioVinos\vinos\django-wine-shop
env\Scripts\activate
python manage.py runserver
```

Verifica que el servidor esté corriendo en: **http://127.0.0.1:8000/**

### Paso 2: Verificar datos de prueba

Asegúrate de que existan los usuarios de prueba ejecutando:

```bash
python seed.py
```

Esto creará:
- **Admin:** usuario: `admin` / contraseña: `Admin12345!`
- **Cliente:** usuario: `cliente1` / contraseña: `Cliente123!`

## 🧪 Ejecutar las Pruebas Funcionales

### En una NUEVA terminal (manteniendo el servidor corriendo):

1. **Activar entorno virtual:**
```bash
cd InventarioVinos\vinos\django-wine-shop
env\Scripts\activate
```

2. **Ejecutar las pruebas:**
```bash
python Pruebas_Funcionales.py
```

## 📸 Capturas de Pantalla

Las pruebas generarán capturas automáticas en:
```
InventarioVinos\vinos\django-wine-shop\Capturas_Completas\
```

Cada captura está numerada secuencialmente y tiene un nombre descriptivo.

## 🎯 Qué Prueba el Script

### ✅ Test 1: Navegación Pública (Sin Login)
- Página principal (Home)
- Catálogo de productos
- Búsqueda de productos
- Detalle de producto
- Sección de ofertas

### ✅ Test 2: Registro de Usuario
- Formulario de registro
- Validación de campos

### ✅ Test 3: Flujo Completo de CLIENTE
- Login de cliente
- Perfil de usuario
- Navegación al catálogo
- Detalle de producto
- Agregar productos al carrito
- Ver carrito
- Proceso de checkout
- Historial de pedidos (Mis Pedidos)
- Logout

### ✅ Test 4: Flujo Completo de ADMINISTRADOR
- Login de administrador
- Panel de administración principal
- **CRUD Productos:** listar, crear, editar
- **CRUD Proveedores:** listar, crear
- **CRUD Pedidos:** listar, editar
- **CRUD Clientes:** listar, crear
- **CRUD Usuarios:** listar
- Generación de reporte Excel
- Consulta de roles
- Perfil de administrador
- Logout

### ✅ Test 5: Verificación Final
- Elementos críticos del sistema (header, footer, navegación)

## 📊 Resultado Esperado

Si todo está correcto, verás:

```
================================================================================
🚀 INICIANDO PRUEBAS FUNCIONALES COMPLETAS DE WINE SHOP
================================================================================

🧪 TEST 1: Navegación de Páginas Públicas (Sin Login)
------------------------------------------------------------
➤ Accediendo a la página principal...
📸 [001] Página principal sin autenticación
  ✓ Encontrados X productos destacados
...

✅ PRUEBAS FINALIZADAS - XX capturas guardadas
📂 Ubicación: Capturas_Completas
================================================================================
```

## ⚠️ Solución de Problemas

### Error: "ChromeDriver no encontrado"
- **Solución:** El script descarga ChromeDriver automáticamente. Asegúrate de tener conexión a Internet.

### Error: "Connection refused" o "Failed to establish connection"
- **Solución:** El servidor Django no está corriendo. Ejecuta `python manage.py runserver` en otra terminal.

### Error: "No se pudo iniciar sesión"
- **Solución:** Verifica que los usuarios existan ejecutando `python seed.py`

### Las pruebas se ejecutan muy rápido
- **Nota:** Los tiempos de espera están optimizados. Si quieres ver más lentamente, aumenta los valores `time.sleep()` en el código.

### Error: "ModuleNotFoundError: No module named 'selenium'"
- **Solución:** Instala las dependencias: `pip install selenium webdriver-manager`

## 📝 Notas Importantes

1. **No cierres** la ventana del navegador durante las pruebas
2. **No muevas** el mouse ni interactúes con el navegador durante las pruebas
3. **Mantén** el servidor Django corriendo en todo momento
4. Las pruebas toman aproximadamente **5-10 minutos** en completarse
5. Se generarán más de **30 capturas** de pantalla

## 🎉 ¡Listo!

Ahora tienes pruebas funcionales completas que verifican TODAS las funcionalidades de Wine Shop de manera automática.

---

**Desarrollado con ❤️ para Wine Shop**






