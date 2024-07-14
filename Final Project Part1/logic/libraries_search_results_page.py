import time

from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LibrariesSearchResultsPage(BasePageApp):
    """
    LibrariesSearchResultsPage class encapsulates functionalities for
    interacting with elements on the library search results page.
    Inherits from BasePageApp.
    """
    LIBRARY_NAME = '//h1[@data-testid="institution-name"]'
    FAVORITE_LIBRARY_BUTTON = '//div[@data-testid="library-favorite-button-section"]'

    def __init__(self, driver):
        """
        Initialize the LibrariesSearchResultsPage class.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)

    def get_library_name(self):
        """
        Get the name of the library.

        :return: The name of the library as text.
        """
        library_name = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARY_NAME))
        )
        return library_name.text

    def click_save_library_to_favorites_button(self):
        """
        Click the button to save the library to favorites.
        """
        # favorite_button = WebDriverWait(self._driver, 15).until(
        #     EC.visibility_of_element_located((By.XPATH, self.FAVORITE_LIBRARY_BUTTON))
        # )
        time.sleep(4)
        self._driver.find_element(By.XPATH, self.FAVORITE_LIBRARY_BUTTON).click()
        time.sleep(5)
