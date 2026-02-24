import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class TestAgregarCarrito(BaseTest):
    def test_agregar_producto_carrito(self):
        # --- Login ---
        self.driver.get(f"{self.base_url}/login/")
        self.wait_and_find_element(By.NAME, "username").send_keys("ana")
        self.wait_and_find_element(By.NAME, "password").send_keys("12345")
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        self.take_screenshot("login_exitoso")

        # --- Ir al catálogo ---
        self.driver.get(f"{self.base_url}/catalogo/")
        time.sleep(2)
        self.take_screenshot("catalogo")

        # --- Seleccionar primer producto disponible ---
        producto = self.wait_and_find_element(By.CSS_SELECTOR, ".producto-item")
        nombre_producto = producto.find_element(By.CSS_SELECTOR, "h3").text.strip()
        self.take_screenshot("seleccion_producto")

        # --- Agregar producto al carrito ---
        boton_agregar = producto.find_element(By.CSS_SELECTOR, "button[type='submit']")
        boton_agregar.click()
        time.sleep(2)
        self.take_screenshot("producto_agregado")

        # --- Ir al carrito ---
        self.driver.get(f"{self.base_url}/carrito/")
        time.sleep(2)
        self.take_screenshot("carrito")

        # --- Verificar producto en carrito ---
        productos_carrito = self.driver.find_elements(By.CSS_SELECTOR, ".item-carrito")
        self.assertTrue(productos_carrito, "❌ No se encontraron productos en el carrito")
        self.assertIn(nombre_producto, self.driver.page_source, "❌ El producto no aparece en el carrito")

if __name__ == '__main__':
    unittest.main()
