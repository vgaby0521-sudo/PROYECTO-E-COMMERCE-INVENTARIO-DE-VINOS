import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class TestLogin(BaseTest):
    def test_login_usuario_existente(self):
        # Navegar a la página de login
        self.driver.get(f"{self.base_url}/login/")
        time.sleep(2)
        self.take_screenshot("login_inicial")

        # Llenar credenciales
        self.wait_and_find_element(By.NAME, "username").send_keys("ana")
        self.wait_and_find_element(By.NAME, "password").send_keys("12345")
        time.sleep(1)
        self.take_screenshot("login_credenciales")

        # Enviar formulario
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        # Verificar login exitoso
        self.assertIn("/home/", self.driver.current_url)
        self.take_screenshot("login_exitoso")
        
        # Verificar que aparece el nombre de usuario
        username_element = self.wait_and_find_element(By.CSS_SELECTOR, ".user-info")
        self.assertIn("ana", username_element.text.lower())

if __name__ == '__main__':
    unittest.main()