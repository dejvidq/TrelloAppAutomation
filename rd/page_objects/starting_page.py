from .login_page import LoginPage
from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_button_control import MobileButtonControl


class StartingPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._login_button = MobileButtonControl(resource_id="id/log_in_button")

    def go_to_login(self):
        self._click(mobile_control=self._login_button)
        return LoginPage(driver=self._driver)

    def is_user_logged_out(self):
        return self._is_element_displayed(mobile_control=self._login_button)
