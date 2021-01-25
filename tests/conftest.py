import random
import string

import pytest
from appium.webdriver.webdriver import WebDriver

from api.api import API
from config_parser import parse_rd_config, get_user_from_config, get_api_key_token
from rd.page_objects.starting_page import StartingPage


@pytest.fixture(autouse=True)
def driver(request) -> WebDriver:
    config = parse_rd_config(conf_file=request.config.getoption('--config'))
    appium_server_url = config.get('appium_server_url')
    caps = config.get('caps')
    driver = WebDriver(command_executor=f"http://{appium_server_url}/wd/hub", desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture()#autouse=True)
def starting_page(driver) -> StartingPage:
    yield StartingPage(driver=driver)


@pytest.fixture(autouse=True)
def user(request) -> tuple:
    return get_user_from_config(conf_file=request.config.getoption('--config'))


@pytest.fixture
def api(request) -> API:
    key, token = get_api_key_token(conf_file=request.config.getoption('--config'))
    api = API(key=key, token=token)
    yield api


@pytest.fixture
def delete_all_boards_after_test(api):
    yield
    api.delete_all_boards()


@pytest.fixture
def create_board(api):
    board_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    api.create_board(board_name=board_name)
    yield board_name
