from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.lenguage_btn = "languageListTriggerId"
        self.lenguages_options = "optionId_languageListOptionsLisId"
        self.pos_btn = "pointOfSaleSelectorId"
        self.pos_options_class = "points-of-sale_list_item_button"
        self.pos_apply_btn = "points-of-sale_footer_action_button"

    def chage_lenguage(self, new_lenguage):
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguage_btn}')]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguages_options}') and .//span[contains(text(), '{new_lenguage}')]]").click()

    def get_selected_lenguage(self):
        html_tag = self.driver.find_element(By.XPATH, "//html")
        lang = html_tag.get_attribute("lang")
        return lang
    
    def chage_pos(self, new_pos):
        self.driver.find_element(By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@class,'{self.pos_options_class}') and .//span[contains(text(), '{new_pos}')]]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@class, '{self.pos_apply_btn}')]").click()

    def get_selected_pos(self):
        pos_selected = self.driver.find_element(By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]")
        return pos_selected.text
