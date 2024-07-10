from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class DeleteListPage(BasePageApp):
    OPTIONS_BUTTON = '//button[@data-testid="list-actions-button"]'
    DELETE_LIST_BUTTON = '//li[@data-testid="menu-item-delete-list"]'
    CONFIRM_DELETE_BUTTON = '//button[@data-testid="delete-list-dialog-button"]'
    NO_LISTS_FOUND_MESSAGE = '//h1[text() = "You do not have any lists on your own"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._options_button = self._driver.find_element(By.XPATH, self.OPTIONS_BUTTON)

    def click_options_button(self):
        self._options_button.click()

    def click_delete_list_button(self):
        delete_list_button = self._driver.find_element(By.XPATH, self.DELETE_LIST_BUTTON)
        delete_list_button.click()

    def click_confirm_delete_button(self):
        confirm_delete_button = self._driver.find_element(By.XPATH, self.CONFIRM_DELETE_BUTTON)
        confirm_delete_button.click()

    def get_no_lists_found_message(self):
        no_lists_found_message = self._driver.find_element(By.XPATH, self.NO_LISTS_FOUND_MESSAGE)
        return no_lists_found_message.is_displayed()
