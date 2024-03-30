import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def pytest_addoption(parser):
    parser.addoption("--browser", default="Chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="192.168.1.6:8081")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None

    if browser_name == "Chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "Firefox":
        options = FireFoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver

    driver.quit()


def is_element_displayed(driver, by, value):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        return True
    except TimeoutException:
        return False
