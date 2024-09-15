import pytest
from pages.home_page import HomePage

@pytest.mark.parametrize("language, lang, opt, expected_url", [
    ("Español", "es", "Información legal", "informacion-legal/informacion-legal/"),
    ("Español", "es", "Política de privacidad", "informacion-legal/politica-privacidad/"),
    ("Español", "es", "Contrato de transporte", "informacion-legal/contrato-de-transporte/"),
    ("Español", "es", "Plan de contingencia", "informacion-legal/plan-de-contingencia/")
])
def test_footer(setup, language, lang, opt, expected_url):
    driver = setup
    driver.get("https://nuxqa6.avtest.ink/")
    home_page = HomePage(driver)
    home_page.chage_lenguage(language)
    home_page.footer_navigate(opt)
    url_found = home_page.get_url()
    assert f"{lang}/{expected_url}" in url_found


