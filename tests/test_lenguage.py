import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("language, expected_lang", [
    ("English", "en"),
    ("Español", "es"),
    ("Français", "fr"),
    ("Português", "pt")
])
def test_change_lenguange(setup, language, expected_lang):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    home_page.chage_lenguage(language)
    lang = home_page.get_selected_lenguage()
    assert lang == expected_lang


