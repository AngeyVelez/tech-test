import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("nav_name, nav_opt, expected_url", [
    ("section-offer", "Ofertas de vuelos", "/es/ofertas-destinos/ofertas-de-vuelos/"),
    ("section-offer", "Destinos", "/es/ofertas-destinos/destinos/"),
    ("section-offer", "Reservas de grupos", "/es/ofertas-destinos/reservas-de-grupos/")
])
def test_nav(setup, nav_name, nav_opt, expected_url):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    home_page.select_navbar_opt(nav_name)
    home_page.nav_navigate(nav_opt)
    url_found = home_page.get_url()
    assert expected_url in url_found


