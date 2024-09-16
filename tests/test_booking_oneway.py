import pytest
import time
from pages.home_page import HomePage
from pages.passengers_page import PassengersPage
from pages.select_flight_page import SelectFlightPage

@pytest.mark.parametrize("journey_type, language, pos, origin, destination", [
    ("1", "Español", "Chile", "PEI", "AUA"),
])
def test_nav(setup, journey_type, language, pos, origin, destination):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    select_flight_page = SelectFlightPage(driver)
    passengers_page = PassengersPage(driver)
    home_page.change_language(language)
    home_page.change_pos(pos)
    home_page.set_journey_type(journey_type)
    home_page.change_origin(origin)
    home_page.change_destination(destination)
    home_page.select_passengers()
    home_page.update_passenger_count(2, "plus")
    home_page.update_passenger_count(3, "plus")
    home_page.update_passenger_count(4, "plus")
    home_page.click_search()
    select_flight_page.select_flight()
    select_flight_page.select_basic_flight()
    select_flight_page.click_continue()
    # form_index, gender, firt_name, last_name, day_brith, month_birth, year_birth, nationality
    passengers_page.fill_passenger_form(1, 1, "Angey", "Velez", 1, 1, 1, 1)
    passengers_page.fill_passenger_form(2, 1, "Juan", "Castro", 2, 2, 2, 2)
    passengers_page.fill_passenger_form(3, 1, "Sweety", "Vela", 3, 3, 3, 3)
    passengers_page.fill_passenger_form(4, 1, "Sandy", "Bedoya", 4, 4, 4, 4)
    time.sleep(10)
    assert 1



