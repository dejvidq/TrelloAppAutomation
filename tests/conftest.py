import pytest
from appium.webdriver.webdriver import WebDriver

from config_parser import parse_rd_config
from rd.page_objects.starting_page import StartingPage


@pytest.fixture(autouse=True)
def driver(request):
    config = parse_rd_config(request.config.getoption('--config'))
    appium_server_url = config.get('appium_server_url')
    caps = config.get('caps')
    driver = WebDriver(f"http://{appium_server_url}/wd/hub", caps)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def starting_page(driver):
    yield StartingPage(driver)
