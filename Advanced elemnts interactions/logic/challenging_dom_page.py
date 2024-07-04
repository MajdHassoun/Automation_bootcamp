from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class ChallengingDomPage(BasePage):
    FIRST_BUTTON = '//a[@class="button"]'
    SECOND_BUTTON = '//a[@class="button alert"]'
    THIRD_BUTTON = '//a[@class="button success"]'
    EDIT_ROW = '//a[text() = "edit"]'
    DELETE_ROW = '//a[text() = "delete"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._first_button = self._driver.find_element(By.XPATH, self.FIRST_BUTTON)
        self._second_button = self._driver.find_element(By.XPATH, self.SECOND_BUTTON)
        self._third_button = self._driver.find_element(By.XPATH, self.THIRD_BUTTON)
        self._edit_row = self._driver.find_elements(By.XPATH, self.EDIT_ROW)
        self._delete_row = self._driver.find_elements(By.XPATH, self.DELETE_ROW)

    def click_on_first_button(self):
        self._first_button.click()

    def click_on_second_button(self):
        self._second_button.click()

    def click_on_third_button(self):
        self._third_button.click()

    def click_on_edit(self, index):
        self._edit_row[index].click()

    def click_on_delete(self, index):
        self._delete_row[index].click()
