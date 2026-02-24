import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time
import os

class TestReporteExcel(BaseTest):
    def test_generar_reporte_excel(self):
        # Login como administrador
        self.driver.get(f"{self.base_url}/login/")
        self.wait_and_find_element(By.NAME, "username").send_keys("admin")
        self.wait_and_find_element(By.NAME, "password").send_keys("admin123")
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Verificar que el botón de reporte existe
        boton_reporte = self.wait_and_find_element(By.CSS_SELECTOR, "a.btn-success")
        self.assertIn("generar reporte excel", boton_reporte.text.lower())
        self.take_screenshot("boton_reporte")

        # Hacer clic en el botón de reporte
        boton_reporte.click()
        time.sleep(3)

        # Verificar que se descargó el archivo (aceptar varios patrones de nombre)
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        archivos = os.listdir(downloads_path)
        # Buscar cualquier .xlsx que contenga palabras clave relacionadas al reporte
        archivo_excel = next((f for f in archivos if f.lower().endswith('.xlsx') and (
            'inventario' in f.lower() or 'reporte_inventario' in f.lower() or 'wineshop' in f.lower() or 'reporte' in f.lower()
        )), None)

        self.assertIsNotNone(archivo_excel, "No se encontró el archivo Excel descargado (buscando patrones flexibles)")
        self.take_screenshot("reporte_generado")

        # Verificar mensaje de éxito
        mensaje = self.wait_and_find_element(By.CSS_SELECTOR, ".message-success")
        self.assertIn("reporte de inventario generado", mensaje.text.lower())

if __name__ == '__main__':
    unittest.main()