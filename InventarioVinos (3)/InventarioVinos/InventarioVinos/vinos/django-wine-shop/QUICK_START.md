# 🚀 Inicio Rápido - Wine Shop

## En pocos pasos, ¡tu tienda de vinos está lista!

### ✅ OPCIÓN 1: Inicio Automático (RECOMENDADO)

**Windows:**
1. Abre `run.bat` haciendo doble clic
2. Espera a que termine
3. Abre http://127.0.0.1:8000

**macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

---

### ✅ OPCIÓN 2: Inicio Manual

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install Django==4.2.7 python-decouple==3.8
python manage.py migrate
python seed.py
python manage.py runserver
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install Django==4.2.7 python-decouple==3.8
python manage.py migrate
python seed.py
python manage.py runserver
```

---

## 🎉 ¡Listo! Tu tienda está en:

- **Tienda:** http://127.0.0.1:8000
- **Admin:** http://127.0.0.1:8000/admin/

---

## 👤 Usuarios para Probar

### Admin
- Usuario: `admin`
- Contraseña: `Admin12345!`

### Cliente
- Usuario: `cliente1`
- Contraseña: `Cliente123!`

---

## 📝 ¿Qué viene después?

1. Explora el catálogo en la página principal
2. Crea una cuenta o inicia sesión
3. Agrega productos al carrito
4. Realiza una compra
5. Accede al admin en `/admin/` para gestionar todo

---

## 🆘 Si algo falla

### Error: "python no encontrado"
Instala Python desde https://www.python.org/downloads/

### Error: "No module named 'django'"
Asegúrate de tener activado el entorno virtual y ejecuta:
```bash
pip install -r requirements.txt
```

### Error: "port already in use"
El puerto 8000 está en uso. Intenta:
```bash
python manage.py runserver 8001
```

---

## 📚 Documentación completa

Ver `README.md` para la guía detallada.

¡Disfruta tu tienda de vinos! 🍷
