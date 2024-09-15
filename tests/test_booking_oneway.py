import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("journey_type, language, pos, origin, destination", [
    ("1", "Español", "Colombia", "PEI", "AUA"),
])
def test_nav(setup, journey_type, language, pos, origin, destination):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    home_page.change_language(language)
    home_page.change_pos(pos)
    home_page.set_journey_type(journey_type)
    home_page.change_origin(origin)
    home_page.change_destination(destination)
    home_page.select_passengers()
    home_page.update_passenger_count(2, "plus")
    home_page.update_passenger_count(3, "plus")
    home_page.update_passenger_count(4, "plus")
    assert 1


