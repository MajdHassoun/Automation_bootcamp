from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class CheckboxesPage(BasePage):
    CHECKBOX_BUTTONS = '//input[@type = "checkbox"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._checkbox_buttons = self._driver.find_elements(By.XPATH, self.CHECKBOX_BUTTONS)

    def click_on_checkbox(self, number=0):
        self._checkbox_buttons[number].click()

    def unclick_checkbox(self, number=0):
        if self._checkbox_buttons[number].is_selected():
            self._checkbox_buttons[number].click()
