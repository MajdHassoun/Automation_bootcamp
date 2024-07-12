from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class DeleteListPage(BasePageApp):
    """
    DeleteListPage class extends BasePageApp and provides methods for interacting with
    elements related to deleting a list.
    """

    # XPaths for elements on the delete list page
    OPTIONS_BUTTON = '//button[@data-testid="list-actions-button"]'
    DELETE_LIST_BUTTON = '//li[@data-testid="menu-item-delete-list"]'
    CONFIRM_DELETE_BUTTON = '//button[@data-testid="delete-list-dialog-button"]'
    NO_LISTS_FOUND_MESSAGE = '//h1[text() = "You do not have any lists on your own"]'

    def __init__(self, driver):
        """
        Initializes the DeleteListPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def click_options_button(self):
        """
        Clicks the options button.

        Uses WebDriverWait to wait up to 10 seconds until the options button is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.OPTIONS_BUTTON))
        )
        element.click()

    def click_delete_list_button(self):
        """
        Clicks the delete list button.

        Uses WebDriverWait to wait up to 10 seconds until the delete list button is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_LIST_BUTTON))
        )
        element.click()

    def click_confirm_delete_button(self):
        """
        Clicks the confirm delete button.

        Uses WebDriverWait to wait up to 10 seconds until the confirm delete button is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_DELETE_BUTTON))
        )
        element.click()

    def get_no_lists_found_message(self):
        """
        Checks if the 'No lists found' message is displayed.

        Uses WebDriverWait to wait up to 10 seconds until the message element is visible.

        :return: True if the message is visible, False otherwise.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_LISTS_FOUND_MESSAGE))
        )
        return element.is_displayed()

    def delete_list_flow(self):
        """
        Executes the flow to delete a list by clicking the options button,
        delete list button, and confirm delete button.
        """
        self.click_options_button()
        self.click_delete_list_button()
        self.click_confirm_delete_button()
