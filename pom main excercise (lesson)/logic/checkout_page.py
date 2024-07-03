from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class CheckoutPage(BasePageApp):
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder = "First Name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder = "Last Name"]')
    ZIP_CODE_INPUT = (By.XPATH, '//input[@placeholder = "Zip/Postal Code"]')
    CANCEL_BUTTON = (By.XPATH, '//button[@id = "cancel"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@id = "continue"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._first_name_input = self._driver.find_element(self.FIRST_NAME_INPUT)
        self._last_name_input = self._driver.find_element(self.LAST_NAME_INPUT)
        self._zip_code_input = self._driver.find_element(self.ZIP_CODE_INPUT)
        self._cancel_button = self._driver.find_element(self.CANCEL_BUTTON)
        self._continue_button = self._driver.find_element(self.CONTINUE_BUTTON)

    def enter_first_name(self, first_name):
        self._first_name_input.clear()
        self._first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        self._last_name_input.clear()
        self._last_name_input.send_keys(last_name)

    def enter_zip_code(self, zip_code):
        self._zip_code_input.clear()
        self._zip_code_input.send_keys(zip_code)

    def click_cancel_button(self):
        self._cancel_button.click()

    def click_continue_button(self):
        self._continue_button.click()

    def checkout_flow(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
