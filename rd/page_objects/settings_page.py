from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class SettingsPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._log_out_button = MobileTextViewControl(resource_id="android:id/title",
                                                     text="Log out",
                                                     is_scrollable=True,
                                                     use_resource_id_prefix=False)

    def log_out(self):
        from .starting_page import StartingPage  # due to circular import
        self._click(mobile_control=self._log_out_button)
        return StartingPage(self._driver)
