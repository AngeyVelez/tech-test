import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("opt, expected_url", [
    ("Información legal", "/es/informacion-legal/informacion-legal/"),
    ("Política de privacidad", "/es/informacion-legal/politica-privacidad/"),
    ("Contrato de transporte", "/es/informacion-legal/contrato-de-transporte/"),
    ("Plan de contingencia", "/es/informacion-legal/plan-de-contingencia/")
])
def test_footer(setup, opt, expected_url):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/es/")
    home_page = HomePage(driver)
    home_page.footer_navigate(opt)
    url_found = home_page.get_url()
    assert expected_url in url_found


