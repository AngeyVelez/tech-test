from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#esta clase se encarga de administrar los navegadores
class DriverManager:
    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'edge':
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError(f"Browser {browser} not supported!")
        return driver
    
