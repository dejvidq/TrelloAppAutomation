from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class SettingsPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._scrollable_parent = MobileControl(is_scrollable=True)
        self._log_out_button = MobileTextViewControl(resource_id="android:id/title",
                                                     text="Log out",
                                                     use_resource_id_prefix=False,
                                                     parent=self._scrollable_parent
                                                     )

    def log_out(self):
        from .starting_page import StartingPage  # due to circular import
        self._click(mobile_control=self._log_out_button)
        return StartingPage(driver=self._driver)
