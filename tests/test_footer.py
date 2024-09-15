import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("opt, expected_url", [
    ("Información legal", "https://nuxqa6.avtest.ink/es/informacion-legal/informacion-legal/"),
    ("Política de privacidad", "https://nuxqa6.avtest.ink/es/informacion-legal/politica-privacidad/"),
    ("Contrato de transporte", "https://nuxqa6.avtest.ink/es/informacion-legal/contrato-de-transporte/"),
    ("Artículos restringidos", "https://ayuda.avianca.com/hc/es/sections/13499643885467")
])
def test_footer(setup, opt, expected_url):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    url_found = home_page.get_footer_opt(opt)
    assert url_found == expected_url


