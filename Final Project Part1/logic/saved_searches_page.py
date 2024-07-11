from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class SavedSearchesPage(BasePageApp):
    NO_SAVED_SEARCHES_MESSAGE = '//p[text()="It seems you haven’t saved any searches yet"]'
    SEARCH_NAME = '//span[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    SAVED_SEARCHES_CHECKBOX = '//input[@name="save-search-select-all"]'
    DELETE_SEARCH_BUTTON = '//button[@data-testid="delete-save-search-button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_no_saved_searches_message(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_SAVED_SEARCHES_MESSAGE)))
        return element.is_displayed()

    def get_search_name(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_NAME)))
        return element.text

    def click_saved_searches_checkbox(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVED_SEARCHES_CHECKBOX)))

        element.click()

    def click_delete_search_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_SEARCH_BUTTON)))

        element.click()

