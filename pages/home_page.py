import time
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.lenguage_btn = "languageListTriggerId"
        self.lenguages_options = "optionId_languageListOptionsLisId"

        self.pos_btn = "pointOfSaleSelectorId"
        self.pos_options = "points-of-sale_list_item_button"
        self.pos_apply_btn = "points-of-sale_footer_action_button"

        self.footer_quick_links = "footerNavListId-3"
        
        self.nav_preffix = "main-header_nav-primary_item--"

    def chage_lenguage(self, new_lenguage):
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguage_btn}')]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@id,'{self.lenguages_options}') and .//span[contains(text(), '{new_lenguage}')]]").click()

    def get_selected_lenguage(self):
        html_tag = self.driver.find_element(By.XPATH, "//html")
        lang = html_tag.get_attribute("lang")
        return lang
    
    def chage_pos(self, new_pos):
        self.driver.find_element(By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@class,'{self.pos_options}') and .//span[contains(text(), '{new_pos}')]]").click()
        self.driver.find_element(By.XPATH, f"//button[contains(@class, '{self.pos_apply_btn}')]").click()

    def get_selected_pos(self):
        pos_selected = self.driver.find_element(By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]")
        return pos_selected.text
    
    def footer_navigate(self, opt):
        self.driver.find_element(By.XPATH, f"//ul[contains(@id, '{self.footer_quick_links}')]/li/a/span[contains(text(), '{opt}')]/parent::a").click() 
    
    def get_url(self):
        time.sleep(2)
        new_url = self.driver.current_url
        return new_url    

    def select_navbar_opt(self, opt_class_suffix):
        self.driver.find_element(By.XPATH, f"//nav/ul/li[contains(@class, '{self.nav_preffix}{opt_class_suffix}')][1]").click() 

    def nav_navigate(self, opt_lbl):
        self.driver.find_element(By.XPATH, f"//header//nav//li[contains(@class, 'is-open')]//li//span[contains(text(),'{opt_lbl}')]/parent::a").click()

    