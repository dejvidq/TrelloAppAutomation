from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class BoardPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._board_name = MobileTextViewControl(resource_id="id/toolbar_title")
        self._board_drawer_right = MobileTextViewControl(resource_id="id/board_sections")
        self._board_settings = MobileTextViewControl(resource_id="id/settings_button")
        self._board_settings_scrollable_parent = MobileControl(resource_id="id/recycler_view",
                                                               is_scrollable=True)
        self._close_board_button = MobileTextViewControl(resource_id="android:id/title",
                                                         use_resource_id_prefix=False,
                                                         text="Close board",
                                                         parent=self._board_settings_scrollable_parent
                                                         )
        self._board_archived_text = MobileTextViewControl(resource_id="id/board_unavailable_text",
                                                          text="Board has been archived.",
                                                          )

    def is_board_created(self, board_name: str) -> bool:
        self._board_name.text = board_name
        return self._is_element_displayed(mobile_control=self._board_name)

    def go_back_to_main_boards_page(self):
        from .main_page import MainPage
        self._driver.back()
        return MainPage(driver=self._driver)

    def open_board_drawer(self):
        self._click(mobile_control=self._board_drawer_right)

    def open_board_settings(self):
        self._click(self._board_settings)

    def close_board(self) -> bool:
        self.open_board_drawer()
        self.open_board_settings()
        self._click(mobile_control=self._close_board_button)
        return self._is_element_displayed(mobile_control=self._board_archived_text)
