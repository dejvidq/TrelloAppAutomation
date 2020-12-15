from appium.webdriver.common.mobileby import MobileBy


class MobileControl:
    def __init__(self, element_selector, locator_strategy: MobileBy = MobileBy.ID):
        self.element_selector = element_selector
        self.locator_strategy = locator_strategy
