from appium.webdriver.common.mobileby import MobileBy

from .mobile_controls.mobile_control import MobileControl
from .mobile_page_abstract_class import MobilePageAbstractClass


class StartingPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._login_button = MobileControl(element_selector="com.trello:id/log_in_button", locator_strategy=MobileBy.ID)

    def log_in(self):
        self._click(self._login_button)
