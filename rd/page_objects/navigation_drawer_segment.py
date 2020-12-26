from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class NavigationDrawerSegment(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._avatar = MobileControl(resource_id="id/avatar_view")
        self._boards_button = MobileTextViewControl(resource_id="id/title", text="Boards")
        self._home_button = MobileTextViewControl(resource_id="id/title", text="Home")
        self._my_cards_button = MobileTextViewControl(resource_id="id/title", text="My Cards")
        self._settigs_button = MobileTextViewControl(resource_id="id/title", text="Settings")
        self._help_button = MobileTextViewControl(resource_id="id/title", text="Help")

    def open_settings(self):
        self._click(mobile_control=self._settigs_button)
