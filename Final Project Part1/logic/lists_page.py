from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class ListsPage(BasePageApp):
    """
    ListsPage class extends BasePageApp and provides methods for interacting with
    elements on the lists page.
    """

    # XPaths for elements on the lists page
    LIST_NAME_BUTTON = '//h3[@data-testid="lists-title"]'
    BOOK_NAME = '//h3[@class="tss-1a1lxt0-ellipsize MuiBox-root mui-0"]'

    def __init__(self, driver):
        """
        Initializes the ListsPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def get_list_name_button(self):
        """
        Retrieves the text from the list name button element.

        Uses WebDriverWait to wait up to 10 seconds until the list name button element is present.

        :return: The text content of the list name button.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.LIST_NAME_BUTTON)))
        return element.text

    def get_book_name(self):
        """
        Retrieves the text from the book name element.

        Uses WebDriverWait to wait up to 10 seconds until the book name element is present.

        :return: The text content of the book name.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.BOOK_NAME)))
        return element.text

    def enter_delete_page(self):
        """
        Clicks on the list name button element to navigate to the delete page.

        Uses WebDriverWait to wait up to 10 seconds until the list name button element is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LIST_NAME_BUTTON)))
        element.click()
