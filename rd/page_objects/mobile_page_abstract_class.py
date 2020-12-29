from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from rd.mobile_controls.mobile_control import MobileControl


class MobilePageAbstractClass:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._resource_id_prefix = "com.trello:"

    def _get_element(self,
                     mobile_control: MobileControl,
                     timeout=10,
                     poll_frequency=0.5,
                     expected_condition: object = expected_conditions.visibility_of_element_located,
                     locator_strategy: str = MobileBy.ANDROID_UIAUTOMATOR
                     ):
        element_selector = mobile_control.get_ui_automator_string(self._resource_id_prefix)
        error_message = f"""After trying for {timeout} second/s with polling every {poll_frequency} second/s,
                            locator strategy '{str(locator_strategy)}' and expected condition {str(expected_condition)}
                            failed to find element via element selector '{element_selector}'"""
        element = None
        try:
            element = WebDriverWait(
                driver=self._driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=None
            ).until(expected_condition((locator_strategy, element_selector)), error_message)
        except Exception as exc:
            raise exc
        finally:
            return element

    def _is_element_displayed(self,
                              mobile_control: MobileControl,
                              timeout=10,
                              poll_frequency=0.5
                              ):
        if self._get_element(mobile_control=mobile_control,
                             timeout=timeout,
                             poll_frequency=poll_frequency
                             ):
            return True
        return False

    def _is_element_enabled(self, mobile_control: MobileControl, timeout=10,
                            poll_frequency=0.5):
        if self._get_element(mobile_control=mobile_control,
                             timeout=timeout,
                             poll_frequency=poll_frequency,
                             expected_condition=expected_conditions.element_to_be_clickable
                             ):
            return True
        return False

    def _wait_for_enable(self, mobile_control: MobileControl, timeout=10,
                         poll_frequency=0.5):
        return self._get_element(mobile_control=mobile_control, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 expected_condition=expected_conditions.element_to_be_clickable)

    def _click(self, mobile_control: MobileControl, timeout=4):
        self._wait_for_enable(mobile_control=mobile_control, timeout=timeout).click()

    def _get_element_attribute(self,
                               mobile_control: MobileControl,
                               attribute: str,
                               ):
        return self._get_element(mobile_control=mobile_control).get_attribute(attribute)

    def _enter_text(self,
                    mobile_control: MobileControl,
                    text: str,
                    press_enter: bool = False,
                    hide_keyboard: bool = False
                    ):
        element = self._get_element(mobile_control=mobile_control)
        element.clear().send_keys(text)
        if press_enter:
            self._driver.press_keycode(66)
        elif hide_keyboard:
            self._driver.hide_keyboard()

    def _get_text(self, mobile_control: MobileControl) -> str:
        return self._get_element(mobile_control=mobile_control).text
