from .login_page import LoginPage
from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_button_control import MobileButtonControl


class StartingPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._login_button = MobileButtonControl(resource_id="id/log_in_button")

    def go_to_login(self):
        self._click(self._login_button)
        return LoginPage(self._driver)
