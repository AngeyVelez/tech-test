# Configuration file and fixtures
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    # Configure the service for ChromeDriver
    service = Service(executable_path="C:\SeleniumDrivers\chromedriver.exe")
    # Start WebDriver for Chrome
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    # Close the browser
    driver.quit()
