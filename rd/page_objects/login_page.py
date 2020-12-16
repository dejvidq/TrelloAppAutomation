from appium.webdriver.common.mobileby import MobileBy

from rd.mobile_controls.mobile_control import MobileControl
from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_button_control import MobileButtonControl
from ..mobile_controls.mobile_edit_field_control import MobileEditFieldControl


class LoginPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._username_field = MobileEditFieldControl(resource_id="id/user")
        self._password_field = MobileEditFieldControl(resource_id="id/password")
        self._login_button = MobileButtonControl(resource_id="id/authenticate")

    def log_in_user(self, username: str, password: str):
        self._click(self._username_field)
        self._enter_text(mobile_control=self._username_field, text=username, press_enter=True)
        self._enter_text(mobile_control=self._password_field, text=password, hide_keyboard=True)
        self._click(self._login_button)
