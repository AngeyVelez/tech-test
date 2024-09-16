# Selenium and Pytest Automation Project

This project is an automated test suite using Selenium and Pytest. It is designed to automate tests for a web application, including flight selection, navigation, and interaction with various page elements.

## Project Structure

```
├── __pycache__/
├── .gitignore
├── .pytest_cache/
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   ├── README.md
│   └── v/
│       └── cache/
├── conftest.py
├── flyr/
│   ├── bin/
│   ├── include/
│   │   └── python3.11/
│   ├── lib/
│   │   └── python3.11/
│   ├── pyvenv.cfg
│   └── Scripts/
│       ├── activate
│       └── ...
├── other_exercises/
│   ├── foobar.py
│   ├── happy_num.py
├── pages/
│   ├── __pycache__/
│   ├── home_page.py
│   ├── passengers_page.py
│   ├── select_flight_page.py
├── README.md
├── requirements.txt
├── tests/
│   ├── __pycache__/
│   ├── test_booking_oneway.py
│   ├── test_footer.py
│   ├── test_language.py
│   ├── test_nav.py
│   ├── test_pos.py
├── utils/
│   ├── __pycache__/
│   ├── form.py
│   ├── helpers.py
```

## Installation

1.  Clone the repository:

    ```sh
    git clone https://github.com/AngeyVelez/tech-test
    cd tech-test
    ```

2.  Create and activate a virtual environment:

    ```sh
    python -m venv flyr
    source flyr/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Directory Structure

- [`conftest.py`](conftest.py): Configuration of fixtures for Pytest.
- [`pages/`](pages/): Contains the Page Object Model (POM) classes for the different pages of the application.
- [`tests/`](tests/): Contains the test files.
- [`utils/`](utils/): Contains utilities and helper functions.

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Usage Example

Here is an example of how to set up and use the test environment in [`conftest.py`](conftest.py):

```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    service = Service(executable_path="C:\SeleniumDrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
```
