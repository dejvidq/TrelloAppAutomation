from .mobile_page_abstract_class import MobilePageAbstractClass
from .navigation_drawer_segment import NavigationDrawerSegment
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_image_button_control import MobileImageButtonControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class SettingsPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._log_out_button = MobileTextViewControl(resource_id="id/title", text="Log out")

    def log_out(self):
        self._click(mobile_control=self._log_out_button)


