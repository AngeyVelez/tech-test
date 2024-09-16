# Configuration file and fixtures
import pytest
from drivers.driver_manager import DriverManager

@pytest.fixture(params=["chrome", "edge", "firefox"])
def setup(request):
    driver = DriverManager.get_driver(request.param)
    driver.maximize_window()
    yield driver
    # Close the browser
    driver.quit()
