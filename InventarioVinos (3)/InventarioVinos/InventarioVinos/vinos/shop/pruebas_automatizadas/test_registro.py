import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class TestRegistro(BaseTest):
    def test_registro_nuevo_usuario(self):
        # Navegar a la página de registro
        self.driver.get(f"{self.base_url}/registro/")
        time.sleep(2)
        self.take_screenshot("registro_inicial")

        # Llenar el formulario
        self.wait_and_find_element(By.NAME, "username").send_keys("usuario_prueba")
        self.wait_and_find_element(By.NAME, "email").send_keys("usuario_prueba@test.com")
        self.wait_and_find_element(By.NAME, "password1").send_keys("Prueba123!")
        self.wait_and_find_element(By.NAME, "password2").send_keys("Prueba123!")
        time.sleep(1)
        self.take_screenshot("registro_form_completo")

        # Enviar el formulario
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Verificar redirección al login
        self.assertIn("/login/", self.driver.current_url)
        self.take_screenshot("redireccion_login")

        # Iniciar sesión con el usuario creado
        self.wait_and_find_element(By.NAME, "username").send_keys("usuario_prueba")
        self.wait_and_find_element(By.NAME, "password").send_keys("Prueba123!")
        time.sleep(1)
        self.take_screenshot("login_nuevo_usuario")

        # Enviar formulario de login
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Verificar login exitoso
        self.assertIn("home", self.driver.current_url)
        self.take_screenshot("login_exitoso")

if __name__ == '__main__':
    unittest.main()
