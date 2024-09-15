import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("pos", [
    ("Otros países"),
    ("España"),
    ("Chile")
])
def test_change_pos(setup, pos):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    home_page.chage_pos(pos)
    country = home_page.get_selected_pos()
    assert pos in country.text


