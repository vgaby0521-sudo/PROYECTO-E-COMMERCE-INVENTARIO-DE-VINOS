import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time
import os

class TestCompra(BaseTest):
    def test_realizar_compra(self):
        # Login primero
        self.driver.get(f"{self.base_url}/login/")
        self.wait_and_find_element(By.NAME, "username").send_keys("ana")
        self.wait_and_find_element(By.NAME, "password").send_keys("12345")
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        
        # Verificar mensaje de bienvenida
        mensaje = self.wait_and_find_element(By.CSS_SELECTOR, ".message-success")
        self.assertIn("bienvenido ana", mensaje.text.lower())
        time.sleep(1)

        # Ir al carrito
        self.driver.get(f"{self.base_url}/carrito/")
        time.sleep(2)
        self.take_screenshot("carrito_inicial")

        # Verificar que hay productos en el carrito
        productos_carrito = self.driver.find_elements(By.CSS_SELECTOR, ".item-carrito")
        self.assertTrue(len(productos_carrito) > 0)

        # Hacer clic en proceder al pago
        self.wait_and_find_element(By.ID, "proceder-pago").click()
        time.sleep(2)
        self.take_screenshot("checkout")

        # Llenar información de envío
        self.wait_and_find_element(By.NAME, "direccion").send_keys("Calle Test 123")
        self.wait_and_find_element(By.NAME, "ciudad").send_keys("Ciudad Test")
        self.wait_and_find_element(By.NAME, "codigo_postal").send_keys("12345")
        time.sleep(1)
        self.take_screenshot("datos_envio")

        # Confirmar compra
        self.wait_and_find_element(By.ID, "confirmar-compra").click()
        time.sleep(2)
        self.take_screenshot("compra_confirmada")

        # Verificar mensaje de éxito
        mensaje = self.wait_and_find_element(By.CSS_SELECTOR, ".mensaje-exito")
        self.assertIn("compra exitosa", mensaje.text.lower())
        
        # Verificar redirección a página de pedido
        self.assertIn("/pedido/", self.driver.current_url)

if __name__ == '__main__':
    unittest.main()