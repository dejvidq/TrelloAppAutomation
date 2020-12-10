import pytest
from appium.webdriver.webdriver import WebDriver


@pytest.fixture(autouse=True)
def driver():
    desired_caps = {
        "appPackage": "com.trello",
        "appActivity": "com.trello.home.HomeActivity",
        "platformName": "Android",
        "platformVersion": "9",
        "udid": "LGH870f9f5fafa"
    }
    driver = WebDriver("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()
