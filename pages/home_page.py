from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lenguage_button = "languageListTriggerId"
        self.lenguages_options = "optionId_languageListOptionsLisId"

    def chage_lenguage(self, new_lenguage):
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguage_button}')]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguages_options}') and .//span[contains(text(), '{new_lenguage}')]]").click()

    def get_selected_lenguage(self):
        html_tag = self.driver.find_element(By.XPATH, "//html")
        lang = html_tag.get_attribute("lang")
        return lang
