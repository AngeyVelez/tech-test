from utils.helpers import wait_for_element
from utils.form import fill_input_text
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PassengersPage:
    
    def __init__(self, driver):
        self.driver = driver

        self.form = "passenger_data_group_item"
        self.genders = "IdPaxGender"
        self.first_name = "IdFirstName"
        self.last_name = "IdLastName"
        self.day_birth = "dateDayId_IdDateOfBirth"
        self.month_birth = "dateMonthId_IdDateOfBirth"
        self.year_birth = "dateYearId_IdDateOfBirth"
        self.nationality = "IdDocNationality"

    def fill_passenger_form(self, form_index, gender, firt_name, last_name, day_birth, month_birth, year_birth, nationality):
        form_xpath = f"//div[contains(@class, '{self.form}')][{form_index}]"
        wait_for_element(self.driver, By.XPATH, f"{form_xpath}//button[contains(@id, '{self.genders}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"({form_xpath}//button[@role='option'])[{gender}]").click()
        input_firt_name = wait_for_element(self.driver, By.XPATH, f"{form_xpath}//input[contains(@id, '{self.first_name}')]", timeout=10)
        fill_input_text(input_firt_name, firt_name)
        input_last_name = wait_for_element(self.driver, By.XPATH, f"{form_xpath}//input[contains(@id, '{self.last_name}')]", timeout=10)
        fill_input_text(input_last_name, last_name)
        print(f"{form_xpath}//button[contains(@id, {self.day_birth})]")
        wait_for_element(self.driver, By.XPATH, f"{form_xpath}//button[contains(@id, '{self.day_birth}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"({form_xpath}//button[@role='option'])[{day_birth}]").click()
        wait_for_element(self.driver, By.XPATH, f"{form_xpath}//button[contains(@id, '{self.month_birth}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"({form_xpath}//button[@role='option'])[{month_birth}]").click()
        wait_for_element(self.driver, By.XPATH, f"{form_xpath}//button[contains(@id, '{self.year_birth}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"({form_xpath}//button[@role='option'])[{year_birth}]").click()
        wait_for_element(self.driver, By.XPATH, f"{form_xpath}//button[contains(@id, '{self.nationality}')]", timeout=10).click()
        wait_for_element(self.driver, By.XPATH, f"({form_xpath}//button[@role='option'])[{nationality}]").click()