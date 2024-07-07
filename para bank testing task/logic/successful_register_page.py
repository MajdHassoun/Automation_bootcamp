from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp


class SuccessfulRegisterPage(BasePageApp):
    WELCOME_USER = '//h1[@class = "title"]'
    CONFIRMATION_MESSAGE = '//p[text()= "Your account was created successfully. You are now logged in."]'

    def __init__(self, driver):
        super().__init__(driver)
        self._welcome_user = self._driver.find_element(By.XPATH, self.WELCOME_USER)
        self._confirmation_message = self._driver.find_element(By.XPATH, self.CONFIRMATION_MESSAGE)

    def welcome_message_displayed(self):
        return self._welcome_user.is_displayed()

    def confirmation_message_displayed(self):
        return self._confirmation_message.is_displayed()

