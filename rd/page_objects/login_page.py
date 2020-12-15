from appium.webdriver.common.mobileby import MobileBy

from rd.mobile_controls.mobile_control import MobileControl
from .mobile_page_abstract_class import MobilePageAbstractClass


class LoginPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._username_field = MobileControl(element_selector="com.trello:id/user")
        self._password_field = MobileControl(element_selector="com.trello:id/password")
        self._login_button = MobileControl(element_selector="com.trello:id/authenticate")

    def log_in_user(self, username: str, password: str):
        self._click(self._username_field)
        self._enter_text(mobile_control=self._username_field, text=username, press_enter=True)
        self._enter_text(mobile_control=self._password_field, text=password, hide_keyboard=True)
        self._click(self._login_button)
