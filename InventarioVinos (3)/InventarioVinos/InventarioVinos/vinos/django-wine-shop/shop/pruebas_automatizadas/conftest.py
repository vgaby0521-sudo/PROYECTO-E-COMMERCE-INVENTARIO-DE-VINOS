import os
import pytest
from datetime import datetime

# Ruta donde se guardarán las capturas
CAPTURE_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "..", "..", "..", "..",
    "captures_unit_tests"
)

os.makedirs(CAPTURE_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que se ejecuta cada vez que termina un test.
    Si falla, toma captura con Selenium.
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_")
            file_path = os.path.join(CAPTURE_DIR, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(file_path)
            print(f"\n📸 Captura guardada: {file_path}")
