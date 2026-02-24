import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


class BaseTest(unittest.TestCase):
    """
    Base de pruebas Selenium.
    Mejorada para integrarse con capturas automáticas desde pytest
    sin afectar el funcionamiento original.
    """

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:8000"

        # Carpeta unificada para pytest + unittest
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
        self.screenshot_dir = os.path.join(project_root, "captures_unit_tests")

        # Crear el directorio si no existe
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

        self.screenshot_counter = 1

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def take_screenshot(self, name):
        """
        Toma una captura manual desde las pruebas.
        pytest también podrá llamar a este método si falla un test.
        """
        filename = f"{self.screenshot_counter:02d}_{name}.png"
        path = os.path.join(self.screenshot_dir, filename)
        
        try:
            self.driver.save_screenshot(path)
            print(f"📸 Captura guardada: {filename}")
        except Exception as e:
            print(f"⚠️ Error guardando captura: {e}")

        self.screenshot_counter += 1

    def wait_and_find_element(self, by, value, timeout=10):
        """Espera y devuelve un elemento."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element


# --- Integración limpia con pytest (NO afecta unittest) ---

def pytest_runtest_makereport(item, call):
    """
    Hook que permite a pytest tomar capturas si un test falla.
    No interfiere con unittest.
    """
    if "self" in item.funcargs:
        test_class = item.funcargs["self"]

        if isinstance(test_class, BaseTest) and call.when == "call":
            if call.excinfo is not None:  # si falló
                test_name = item.name.replace("/", "_")
                try:
                    test_class.take_screenshot(f"ERROR_{test_name}")
                except:
                    pass
