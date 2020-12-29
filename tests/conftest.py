import pytest
from appium.webdriver.webdriver import WebDriver

from api.api import API
from config_parser import parse_rd_config, get_user_from_config, get_api_key_token
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


@pytest.fixture(autouse=True)
def user(request):
    return get_user_from_config(request.config.getoption('--config'))


@pytest.fixture
def api(request):
    key, token = get_api_key_token(request.config.getoption('--config'))
    api = API(key=key, token=token)
    yield api


@pytest.fixture
def delete_all_boards_after_test(api):
    yield
    api.delete_all_boards()
