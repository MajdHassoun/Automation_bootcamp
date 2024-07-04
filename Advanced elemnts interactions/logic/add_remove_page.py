from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    ADD_ELEMENTS_BUTTON = '//button[@onclick="addElement()"]'
    DELETE_ELEMENTS_BUTTON = 'added-manually'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_elements_button = self._driver.find_element(By.XPATH, self.ADD_ELEMENTS_BUTTON)

    def click_on_add_elements(self):
        self._add_elements_button.click()

    def click_on_add_elements_counts(self, count):
        for i in range(count):
            self.click_on_add_elements()

    def click_on_delete(self, index=0):
        buttons_list = self._driver.find_elements(By.CLASS_NAME, self.DELETE_ELEMENTS_BUTTON)
        buttons_list[index].click()
