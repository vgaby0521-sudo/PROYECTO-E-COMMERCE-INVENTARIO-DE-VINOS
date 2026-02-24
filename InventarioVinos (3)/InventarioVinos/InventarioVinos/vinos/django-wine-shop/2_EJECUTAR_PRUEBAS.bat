@echo off
echo ================================================================================
echo EJECUTANDO PRUEBAS FUNCIONALES - WINE SHOP
echo ================================================================================
echo.
echo Verificando que el servidor este corriendo...
timeout /t 2 /nobreak > nul
echo.
echo Activando entorno virtual...
call env\Scripts\activate.bat
echo.
echo IMPORTANTE: Asegurate de que el servidor este corriendo en otra ventana
echo             (Ejecuta 1_INICIAR_SERVIDOR.bat primero)
echo.
echo Presiona cualquier tecla para iniciar las pruebas...
pause > nul
echo.
echo Iniciando pruebas funcionales...
echo Las capturas se guardaran en: Capturas_Completas\
echo.
echo ================================================================================
python Pruebas_Funcionales.py
echo.
echo ================================================================================
echo PRUEBAS COMPLETADAS
echo ================================================================================
echo.
echo Las capturas estan disponibles en: Capturas_Completas\
echo.
pause








