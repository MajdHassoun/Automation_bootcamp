from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class SavedSearchesPage(BasePageApp):
    NO_SAVED_SEARCHES_MESSAGE = '//p[text()="It seems you haven’t saved any searches yet"]'
    SEARCH_NAME = '//span[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    SAVED_SEARCHES_CHECKBOX = '//input[@name="save-search-select-all"]'
    DELETE_SEARCH_BUTTON = '//button[@data-testid="delete-save-search-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._search_name = self._driver.find_element(By.XPATH, self.SEARCH_NAME)
        self._saved_searches_checkbox = self._driver.find_element(By.XPATH, self.SAVED_SEARCHES_CHECKBOX)
        self._delete_search_button = self._driver.find_element(By.XPATH, self.DELETE_SEARCH_BUTTON)

    def get_no_saved_searches_message(self):
        no_saved_searches_message = self._driver.find_element(By.XPATH, self.NO_SAVED_SEARCHES_MESSAGE)
        return no_saved_searches_message.is_displayed()

    def get_search_name(self):
        return self._search_name.text

    def click_saved_searches_checkbox(self):
        self._saved_searches_checkbox.click()

    def click_delete_search_button(self):
        self._delete_search_button.click()


