@echo off
echo ================================================================================
echo INICIANDO SERVIDOR DJANGO - WINE SHOP
echo ================================================================================
echo.
echo Activando entorno virtual...
call env\Scripts\activate.bat
echo.
echo Iniciando servidor en http://127.0.0.1:8000/
echo.
echo IMPORTANTE: NO CIERRES ESTA VENTANA
echo             Deja el servidor corriendo mientras ejecutas las pruebas
echo.
echo ================================================================================
python manage.py runserver
pause








