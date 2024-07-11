from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class SecondSignInPage(BasePage):
    EMAIL_INPUT = '//input[@name = "signin.username"]'
    PASSWORD_INPUT = '//input[@name = "signin.password"]'
    SIGNIN_BUTTON = '//button[@id = "submitSignin"]'
    ERROR_MESSAGE = '//div[text()= "The email or password is invalid. Authentication failed."]'
    SIGN_IN_PAGE_TITLE = '//span[@title = "My Account in the European Data Center"]'

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT)))

        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        password_input = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT))
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_signin_second_page(self):
        signin_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON))
        )
        signin_button.click()

    def get_error_message(self):
        return WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE))
        ).text

    def get_sign_in_page_title(self):
        return WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.SIGN_IN_PAGE_TITLE))
        ).text

    def second_signin_flow(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin_second_page()
