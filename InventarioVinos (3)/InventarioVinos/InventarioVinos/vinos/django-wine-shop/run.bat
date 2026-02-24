@echo off
REM Wine Shop - Script de inicio para Windows
setlocal enabledelayedexpansion

echo ================================
echo Wine Shop - Tienda de Vinos
echo ================================

REM Verificar si existe el entorno virtual
if not exist "venv" (
    echo.
    echo Creando entorno virtual...
    python -m venv venv
    if !errorlevel! neq 0 (
        echo ERROR: No se pudo crear el entorno virtual
        echo Asegúrate de que Python está instalado
        pause
        exit /b 1
    )
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Instalar dependencias
echo.
echo Instalando dependencias...
pip install Django==4.2.7 python-decouple==3.8
if !errorlevel! neq 0 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

REM Realizar migraciones
echo.
echo Realizando migraciones...
python manage.py migrate
if !errorlevel! neq 0 (
    echo ERROR: Error en las migraciones
    pause
    exit /b 1
)

REM Verificar si existen datos de prueba
if not exist "db.sqlite3" (
    echo Poblando base de datos con datos de prueba...
    python seed.py
)

REM Iniciar servidor
echo.
echo ================================
echo Iniciando servidor...
echo URL: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin/
echo ================================
echo.

python manage.py runserver
