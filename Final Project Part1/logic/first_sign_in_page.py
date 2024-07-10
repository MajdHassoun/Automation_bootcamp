from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from logic.utils import Utils


class FirstSignInPage(BasePage):
    EMAIL_INPUT = '//input[@name = "emailField"]'
    CONTINUE_BUTTON = '//button[@type = "submit"]'
    PAGE_TITLE = '//h1[text()="Welcome to WorldCat.org"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._continue_button = self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)
        self._page_title = self._driver.find_element(By.XPATH, self.PAGE_TITLE)
        self.init_page()

    def init_page(self):
        Utils.wait_for_element(self._page_title.is_displayed(), True, 2, 10)

    def enter_email(self, email):
        self._email_input.clear()
        self._email_input.send_keys(email)

    def click_continue(self):
        self._continue_button.click()

    def first_signin_flow(self, email):
        self.enter_email(email)
        self.click_continue()
