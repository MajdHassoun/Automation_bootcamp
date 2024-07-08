from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class SignInPage(BasePage):
    EMAIL_PHONE_INPUT = '//input[@type = "email"]'
    NEXT_BUTTON = '(//button[@type = "button" and @jsname="LgbsSe"])[2]'
    PASSWORD_INPUT = '//input[@name="Passwd"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_phone_input = self._driver.find_element(By.XPATH, self.EMAIL_PHONE_INPUT)

    def enter_email_phone(self, email_or_phone):
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.EMAIL_PHONE_INPUT)))
        self._email_phone_input.clear()
        self._email_phone_input.send_keys(email_or_phone)

    def click_next_button(self):
        element = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.NEXT_BUTTON)))
        element.click()

    def enter_password(self, password):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        element.send_keys(password)

    def sign_in(self, email_or_phone, password):
        self.enter_email_phone(email_or_phone)
        self.click_next_button()
        self.enter_password(password)
        self.click_next_button()
