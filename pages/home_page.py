import time
from utils.helpers import wait_for_element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver

        self.language_btn = "languageListTriggerId"
        self.languages_options = "optionId_languageListOptionsLisId"
        self.pos_btn = "pointOfSaleSelectorId"
        self.pos_options = "points-of-sale_list_item_button"
        self.pos_apply_btn = "points-of-sale_footer_action_button"
        self.footer_quick_links = "footerNavListId-3"
        self.nav_preffix = "main-header_nav-primary_item--"
        self.journey_type = "journeytypeId_"
        self.origin_btn = "originBtn"
        self.origin_div = "originDiv"
        self.destination_path = "arrivalStationInputLabel"
        self.passengers_btn = "paxControlSearchId"
        self.search_btn = "searchButton"

    def change_language(self, new_lenguage):
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@id,'{self.language_btn}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@id,'{self.languages_options}') and .//span[contains(text(), '{new_lenguage}')]]", timeout=10).click()

    def get_selected_language(self):
        html_tag = wait_for_element(self.driver,By.XPATH, "//html", timeout=10)
        lang = html_tag.get_attribute("lang")
        return lang
    
    def change_pos(self, new_pos):
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@class,'{self.pos_options}') and .//span[contains(text(), '{new_pos}')]]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@class, '{self.pos_apply_btn}')]", timeout=10).click()

    def get_selected_pos(self):
        pos_selected = wait_for_element(self.driver, By.XPATH, f"//button[contains(@id, '{self.pos_btn}')]", timeout=10)
        return pos_selected.text
    
    def footer_navigate(self, opt):
        wait_for_element(self.driver, By.XPATH, f"//ul[contains(@id, '{self.footer_quick_links}')]/li/a/span[contains(text(), '{opt}')]/parent::a", timeout=10).click() 
    
    def get_url(self):
        time.sleep(3)
        new_url = self.driver.current_url
        return new_url    

    def select_navbar_opt(self, opt_class_suffix):
        wait_for_element(self.driver, By.XPATH, f"//nav/ul/li[contains(@class, '{self.nav_preffix}{opt_class_suffix}')][1]", timeout=10).click() 

    def nav_navigate(self, opt_lbl):
        wait_for_element(self.driver, By.XPATH, f"//header//nav//li[contains(@class, 'is-open')]//li//span[contains(text(),'{opt_lbl}')]/parent::a", timeout=10).click()

    #type 0 = round trip | 1 = one-way
    def set_journey_type(self, type):
        wait_for_element(self.driver, By.XPATH, f"//input[contains(@id, '{self.journey_type}{type}')]", timeout=10).click()

    def change_origin(self, origin_code):
        #se debe dar click al button para que se habilite el input
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@id, '{self.origin_btn}')]", timeout=10).click()
        input_origin = wait_for_element(self.driver, By.XPATH, f"//div[contains(@id, '{self.origin_div}')]/input", timeout=10)
        input_origin.send_keys(origin_code)
        input_origin.send_keys(Keys.ENTER)
    
    def change_destination(self, destination_code):
        input_origin = wait_for_element(self.driver, By.XPATH, f"//div[contains(@id,'{self.destination_path}')]/following-sibling::input", timeout=10)
        input_origin.send_keys(destination_code)
        input_origin.send_keys(Keys.ENTER)

    def select_passengers(self):
        wait_for_element(self.driver, By.XPATH, f"//div[contains(@class, 'pax-control')]//button[@class = 'control_field_button']", timeout=10).click()

    # type 1 = adult | 2 = young | 3 = child | 4 = infant
    # operator minus | plus
    def update_passenger_count(self, type, operator):
        wait_for_element(self.driver, By.XPATH, f"//div[@id='{self.passengers_btn}']//li[{type}]//button[contains(@class, '{operator}')]", timeout=10).click()

    def click_search(self):
        wait_for_element(self.driver, By.ID, self.search_btn, timeout=10).click()
