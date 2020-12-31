from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class BoardPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver)
        self._board_name = MobileTextViewControl(resource_id="id/toolbar_title")

    def is_board_created(self, board_name: str) -> bool:
        self._board_name.text = board_name
        return self._is_element_displayed(mobile_control=self._board_name)

    def go_back_to_main_boards_page(self):
        from .main_page import MainPage
        self._driver.back()
        return MainPage(self._driver)
