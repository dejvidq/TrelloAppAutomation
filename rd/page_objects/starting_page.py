from rd.mobile_controls.mobile_control import MobileControl
from .login_page import LoginPage
from .mobile_page_abstract_class import MobilePageAbstractClass


class StartingPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._login_button = MobileControl(element_selector="com.trello:id/log_in_button")

    def go_to_login(self):
        self._click(self._login_button)
        return LoginPage(self._driver)
