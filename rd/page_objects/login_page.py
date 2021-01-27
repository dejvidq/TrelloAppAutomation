from .main_page import MainPage
from .mobile_page_abstract_class import MobilePageAbstractClass
from ..mobile_controls.mobile_button_control import MobileButtonControl
from ..mobile_controls.mobile_control import MobileControl
from ..mobile_controls.mobile_edit_field_control import MobileEditFieldControl
from ..mobile_controls.mobile_text_view_control import MobileTextViewControl


class LoginPage(MobilePageAbstractClass):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self._username_field = MobileEditFieldControl(resource_id="id/user")
        self._password_field = MobileEditFieldControl(resource_id="id/password")
        self._login_button = MobileButtonControl(resource_id="id/authenticate")
        self._wrong_password_error_popup = MobileControl(resource_id="id/parentPanel")
        self._wrong_password_error_message = MobileTextViewControl(
            text="The password you entered is invalid. Please try again or reset your password.",
            resource_id="android:id/message",
            use_resource_id_prefix=False,
            parent=self._wrong_password_error_popup
        )
        self._chrome_open_always = MobileButtonControl(resource_id="android:id/button_always",
                                                       use_resource_id_prefix=False
                                                       )
        self._choose_or_add_account = MobileControl(description="Choose or add another account",
                                                    use_resource_id_prefix=False)
        self._webview_email_field = MobileEditFieldControl(resource_id="username",
                                                           use_resource_id_prefix=False
                                                           )
        self._webview_password_field = MobileEditFieldControl(resource_id="password",
                                                              use_resource_id_prefix=False
                                                              )
        self._webview_continue_button = MobileButtonControl(resource_id="login-submit",
                                                            use_resource_id_prefix=False
                                                            )

    def log_in_user(self, username: str, password: str) -> MainPage:
        self._click(mobile_control=self._username_field)
        self._enter_text(mobile_control=self._username_field, text=username, press_enter=True)
        if self._is_element_displayed(mobile_control=self._password_field):
            self._enter_text(mobile_control=self._password_field, text=password, hide_keyboard=True)
            self._click(mobile_control=self._login_button)
        else:
            if self._is_element_displayed(mobile_control=self._chrome_open_always):
                self._click(mobile_control=self._chrome_open_always)
            if self._is_element_displayed(self._choose_or_add_account):
                self._click(mobile_control=MobileControl(description=username))
            else:
                self._wait_for_element(mobile_control=self._webview_email_field)
                self._enter_text(mobile_control=self._webview_email_field,
                                 text=username,
                                 hide_keyboard=True
                                 )
                self._click(mobile_control=self._webview_continue_button)
                self._enter_text(mobile_control=self._webview_password_field,
                                 text=password,
                                 press_enter=True
                                 )
        return MainPage(driver=self._driver)

    def is_wrong_password_error_shown(self) -> bool:
        return self._is_element_displayed(mobile_control=self._wrong_password_error_message)
