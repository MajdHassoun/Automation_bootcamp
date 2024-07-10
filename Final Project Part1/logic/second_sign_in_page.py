from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage
from logic.utils import Utils


class SecondSignInPage(BasePage):
    EMAIL_INPUT = '//input[@name = "signin.username"]'
    PASSWORD_INPUT = '//input[@name = "signin.password"]'
    SIGNIN_BUTTON = '//button[@id = "submitSignin"]'
    ERROR_MESSAGE = '//div[text()= "The email or password is invalid. Authentication failed."]'
    SIGN_IN_PAGE_TITLE = '//span[@title = "My Account in the European Data Center"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._signin_button = self._driver.find_element(By.XPATH, self.SIGNIN_BUTTON)
        self._sign_in_page_title = self._driver.find_element(By.XPATH, self.SIGN_IN_PAGE_TITLE)
        self.init_page()

    def init_page(self):
        Utils.wait_for_element(self._sign_in_page_title.is_displayed(), True, 2, 10)

    def enter_email(self, email):
        self._email_input.clear()
        self._email_input.send_keys(email)

    def enter_password(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)

    def click_signin_second_page(self):
        self._signin_button.click()

    def second_signin_flow(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin_second_page()

    def error_message_display(self):
        error_message = self._driver.find_element(By.XPATH, self.ERROR_MESSAGE)
        return error_message.is_displayed()
