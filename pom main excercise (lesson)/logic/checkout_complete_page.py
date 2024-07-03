from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class CheckoutCompletePage(BasePageApp):
    BACK_HOME_BUTTON = (By.XPATH, '//button[@data-test="back-to-products"]')
    CONFIRMATION_MESSAGE = (By.XPATH, '//h2[@data-test="complete-header"]')
    SUB_CONFIRMATION_MESSAGE = (By.XPATH, '//div[@data-test="complete-text"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._back_home_button = self._driver.find_element(self.BACK_HOME_BUTTON)
        self._confirmation_message = self._driver.find_element(self.CONFIRMATION_MESSAGE)
        self._sub_confirmation_message = self._driver.find_element(self.SUB_CONFIRMATION_MESSAGE)

    def click_back_home_button(self):
        self._back_home_button.click()

    def get_confirmation_message(self):
        return self._confirmation_message.text

    def get_sub_confirmation_message(self):
        return self._sub_confirmation_message.text
