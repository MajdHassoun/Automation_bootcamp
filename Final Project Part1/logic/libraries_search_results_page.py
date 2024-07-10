from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class LibrariesSearchResultsPage(BasePageApp):
    LIBRARY_NAME = '//h1[@data-testid="institution-name"]'
    FAVORITE_LIBRARY_BUTTON = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium mui-15mydm5"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._library_name = self._driver.find_element(By.XPATH, self.LIBRARY_NAME)
        self._favorite_library_button = self._driver.find_element(By.XPATH, self.FAVORITE_LIBRARY_BUTTON)

    def get_library_name(self):
        return self._library_name.text

    def display_library_name(self):
        return self._library_name.is_displayed()

    def click_favorite_library_button(self):
        self._favorite_library_button.click()
