from .board_page import BoardPage
from .mobile_page_abstract_class import MobilePageAbstractClass
from .navigation_drawer_segment import NavigationDrawerSegment
from .settings_page import SettingsPage
from ..mobile_controls.mobile_button_control import MobileButtonControl
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_edit_field_control import MobileEditFieldControl
from ..mobile_controls.mobile_image_button_control import MobileImageButtonControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class MainPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._page_title = MobileTextViewControl(text="Boards")
        self._toolbar_control = MobileControl(resource_id="id/toolbar")
        self._drawer_button = MobileImageButtonControl(description="Open Drawer")
        self._drawer_segment = NavigationDrawerSegment(driver)
        self._add_button = MobileImageButtonControl(resource_id="id/add_fab")
        self._add_board = MobileImageButtonControl(resource_id="id/add_board_fab")
        self._add_card = MobileImageButtonControl(resource_id="id/add_card_fab")
        self._board_name_edit_field = MobileEditFieldControl(resource_id="id/board_name")
        self._visibility_spinner = MobileControl(resource_id="id/visibility_spinner")
        self._selected_visibility = MobileTextViewControl(resource_id="android:id/text1",
                                                          parent=self._visibility_spinner,
                                                          use_resource_id_prefix=False)
        self._visibility_parent = MobileControl(resource_id="id/container")
        self._private_board_text_view = MobileControl(resource_id="android:id/text1",
                                                      text="Private",
                                                      parent=self._visibility_parent,
                                                      use_resource_id_prefix=False
                                                      )
        self._public_board_text_view = MobileControl(resource_id="id/text1",
                                                     text="Public",
                                                     parent=self._visibility_parent,
                                                     use_resource_id_prefix=False
                                                     )
        self._team_board_text_view = MobileControl(resource_id="id/text1",
                                                   text="Public",
                                                   parent=self._visibility_parent,
                                                   use_resource_id_prefix=False
                                                   )
        self._create_board = MobileButtonControl(resource_id="id/create_board")
        self._board_control = MobileTextViewControl(resource_id="id/board_name",
                                                    parent=MobileControl(
                                                        resource_id="id/board_row_view"
                                                    ))

    def is_logged_in(self) -> bool:
        return self._is_element_displayed(mobile_control=self._page_title) and self._is_element_displayed(
            mobile_control=self._toolbar_control)

    def open_drawer(self) -> None:
        self._click(mobile_control=self._drawer_button)

    def open_settings(self) -> SettingsPage:
        self.open_drawer()
        self._drawer_segment.open_settings()
        return SettingsPage(driver=self._driver)

    def add_board(self, board_name: str, visibility: str = "Private") -> BoardPage:
        self._click(mobile_control=self._add_button)
        self._click(mobile_control=self._add_board)
        self._enter_text(mobile_control=self._board_name_edit_field, text=board_name, hide_keyboard=True)
        if self._get_text(mobile_control=self._selected_visibility) != visibility:
            self._click(mobile_control=self._visibility_spinner)
            if visibility == "Private":
                self._click(mobile_control=self._private_board_text_view)
            elif visibility == "Public":
                self._click(mobile_control=self._public_board_text_view)
            elif visibility == "Team":
                self._click(mobile_control=self._team_board_text_view)
        self._click(mobile_control=self._create_board)
        return BoardPage(driver=self._driver)

    def is_board_visible(self, board_name: str) -> bool:
        self._board_control.text = board_name
        return self._is_element_displayed(self._board_control)
