from .mobile_page_abstract_class import MobilePageAbstractClass
from .navigation_drawer_segment import NavigationDrawerSegment
from .settings_page import SettingsPage
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_image_button_control import MobileImageButtonControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class BoardsPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._page_title = MobileTextViewControl(text="Boards")
        self._toolbar_control = MobileControl(resource_id="id/toolbar")
        self._drawer_button = MobileImageButtonControl(description="Open Drawer")
        self._drawer_segment = NavigationDrawerSegment(driver)

    def is_logged_in(self) -> bool:
        return self._is_element_displayed(mobile_control=self._page_title) and self._is_element_displayed(
            mobile_control=self._toolbar_control)

    def open_drawer(self):
        self._click(mobile_control=self._drawer_button)

    def open_settings(self):
        self.open_drawer()
        self._drawer_segment.open_settings()
        return SettingsPage(self._driver)


