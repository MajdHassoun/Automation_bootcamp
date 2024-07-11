import time

from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LibrariesSearchResultsPage(BasePageApp):
    LIBRARY_NAME = '//h1[@data-testid="institution-name"]'
    FAVORITE_LIBRARY_BUTTON = '//button[@data-testid="library-favorite-icon-216413"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_library_name(self):
        library_name = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARY_NAME))
        )
        return library_name.text

    def click_save_library_to_favorites_button(self):
        favorite_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.FAVORITE_LIBRARY_BUTTON))
        )
        favorite_button.click()
        time.sleep(10)
