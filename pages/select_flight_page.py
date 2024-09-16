from utils.helpers import wait_for_element, wait_for_clickable_element
from selenium.webdriver.common.by import By

class SelectFlightPage:
    
    def __init__(self, driver):
        self.driver = driver

        self.price_btn = "journey_price_button"
        self.journey_fare = "fare-control"
        self.continue_btn = "page_button-primary-flow"
    
    def select_flight(self):
        wait_for_element(self.driver, By.XPATH, f"//button[contains(@class,'{self.price_btn}')]", timeout=10).click()

    def select_basic_flight(self):
        wait_for_element(self.driver, By.XPATH, f"//{self.journey_fare}//div", timeout=10).click()

    def click_continue(self):
        print("aquiiiii!!!! POR FAVAAARR ", f"//button[contains(@class, '{self.continue_btn}')]")
        wait_for_clickable_element(self.driver, By.XPATH, f"//button[contains(@class, '{self.continue_btn}')]", timeout=5000).click()

