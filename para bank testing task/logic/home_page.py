from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class HomePage(BasePageApp):
    REGISTER_BUTTON = '//a[text() = "Register"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def click_register_button(self):
        self._register_button.click()
