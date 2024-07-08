from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BeforeSigninHomePage(BasePage):
    SEARCH_INPUT_BAR = '//input[@id = "search"]'
    SIGN_IN_BUTTON = '(//yt-button-shape//a)[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._search_input_bar = driver.find_element(By.XPATH, self.SEARCH_INPUT_BAR)
        self._sign_in_button = driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

    def enter_search_text(self, search_text: str):
        self._search_input_bar.clear()
        self._search_input_bar.send_keys(search_text)

    def click_sign_in_button(self):
        self._sign_in_button.click()
