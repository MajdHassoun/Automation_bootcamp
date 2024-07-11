from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class FirstSignInPage(BasePage):
    EMAIL_INPUT = '//input[@name = "emailField"]'
    CONTINUE_BUTTON = '//button[@type = "submit"]'
    PAGE_TITLE = '//h1[text()="Welcome to WorldCat.org"]'

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_input = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT))
        )
        email_input.clear()
        email_input.send_keys(email)

    def click_continue(self):
        continue_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        )
        continue_button.click()

    def get_page_title(self):
        page_title = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))
        )
        return page_title.text

    def first_signin_flow(self, email):
        self.enter_email(email)
        self.click_continue()
