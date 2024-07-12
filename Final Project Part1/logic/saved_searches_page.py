from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class SavedSearchesPage(BasePageApp):
    """
    SavedSearchesPage class extends BasePageApp and provides methods for interacting with
    elements on the saved searches page.
    """

    # XPaths for elements on the saved searches page
    NO_SAVED_SEARCHES_MESSAGE = '//p[text()="It seems you haven’t saved any searches yet"]'
    SEARCH_NAME = '//span[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    SAVED_SEARCHES_CHECKBOX = '//input[@name="save-search-select-all"]'
    DELETE_SEARCH_BUTTON = '//button[@data-testid="delete-save-search-button"]'

    def __init__(self, driver):
        """
        Initializes the SavedSearchesPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def get_no_saved_searches_message(self):
        """
        Checks if the message indicating no saved searches is displayed.

        Uses WebDriverWait to wait up to 10 seconds until the message element is visible.

        :return: True if the message is displayed, False otherwise.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_SAVED_SEARCHES_MESSAGE)))
        return element.is_displayed()

    def get_search_name(self):
        """
        Retrieves the text from the search name element.

        Uses WebDriverWait to wait up to 10 seconds until the search name element is visible.

        :return: The text content of the search name.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_NAME)))
        return element.text

    def click_saved_searches_checkbox(self):
        """
        Clicks on the saved searches checkbox element.

        Uses WebDriverWait to wait up to 10 seconds until the checkbox element is visible.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SAVED_SEARCHES_CHECKBOX)))

        element.click()

    def click_delete_search_button(self):
        """
        Clicks on the delete search button element.

        Uses WebDriverWait to wait up to 10 seconds until the delete button element is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_SEARCH_BUTTON)))
        element.click()
