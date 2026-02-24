import unittest
from .base_test import BaseTest
from selenium.webdriver.common.by import By
import time

class TestLogout(BaseTest):
    def test_logout(self):
        # Login primero
        self.driver.get(f"{self.base_url}/login/")
        self.wait_and_find_element(By.NAME, "username").send_keys("ana")
        self.wait_and_find_element(By.NAME, "password").send_keys("12345")
        self.wait_and_find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        self.take_screenshot("antes_logout")

        # Hacer clic en el botón de logout
        self.wait_and_find_element(By.ID, "logout-btn").click()
        time.sleep(2)
        self.take_screenshot("despues_logout")

        # Verificar redirección al login
        self.assertIn("/login/", self.driver.current_url)
        
        # Verificar que ya no hay acceso a páginas protegidas
        self.driver.get(f"{self.base_url}/perfil/")
        time.sleep(1)
        self.assertIn("/login/", self.driver.current_url)
        self.take_screenshot("redireccion_protegida")

if __name__ == '__main__':
    unittest.main()