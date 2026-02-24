#!/bin/bash

# Wine Shop - Script de inicio

echo "================================"
echo "Wine Shop - Tienda de Vinos"
echo "================================"

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Realizar migraciones
echo "Realizando migraciones..."
python manage.py migrate

# Verificar si existen datos de prueba
if [ ! -f "db.sqlite3" ] || [ ! -s "db.sqlite3" ]; then
    echo "Poblando base de datos con datos de prueba..."
    python seed.py
fi

# Iniciar servidor
echo ""
echo "================================"
echo "Iniciando servidor..."
echo "URL: http://127.0.0.1:8000"
echo "Admin: http://127.0.0.1:8000/admin/"
echo "================================"
echo ""

python manage.py runserver
