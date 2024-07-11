from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class DeleteListPage(BasePageApp):
    OPTIONS_BUTTON = '//button[@data-testid="list-actions-button"]'
    DELETE_LIST_BUTTON = '//li[@data-testid="menu-item-delete-list"]'
    CONFIRM_DELETE_BUTTON = '//button[@data-testid="delete-list-dialog-button"]'
    NO_LISTS_FOUND_MESSAGE = '//h1[text() = "You do not have any lists on your own"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_options_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.OPTIONS_BUTTON)))
        element.click()

    def click_delete_list_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_LIST_BUTTON)))
        element.click()

    def click_confirm_delete_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_DELETE_BUTTON)))

        element.click()

    def get_no_lists_found_message(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_BUTTON)))
        return element.is_displayed()

    def delete_list_flow(self):
        self.click_options_button()
        self.click_delete_list_button()
        self.click_confirm_delete_button()
