import time

from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class DropDownListPage(BasePage):
    DROPDOWN_WINDOW = '//select[@id="dropdown"]'
    OPTION_ONE = '//option[@value="1"]'
    OPTION_TWO = '//option[@value="2"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._dropdown_window = self._driver.find_element(By.XPATH, self.DROPDOWN_WINDOW)
        self._option_one = self._driver.find_element(By.XPATH, self.OPTION_ONE)
        self._option_two = self._driver.find_element(By.XPATH, self.OPTION_TWO)

    def pick_option_one(self):
        self._dropdown_window.click()
        self._option_one.click()

    def pick_option_two(self):
        self._dropdown_window.click()
        self._option_two.click()

    def pick_both_options_flow(self):
        self.pick_option_one()
        time.sleep(0.5)
        self.pick_option_two()

