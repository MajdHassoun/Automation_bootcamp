from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BeforeLoginHomePage(BasePage):
    SEARCH_INPUT_BAR = '//input[@id = "search"]'
    SIGN_IN_BUTTON = '//div[@id = "end"]//a[@aria-label="Sign in"]'

    def __init__(self, driver):
        super().__init__(driver)

        self._sign_in_button = driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

    def click_sign_in_button(self):
        self._sign_in_button.click()
