from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class ListsPage(BasePageApp):
    LIST_NAME_BUTTON = '//h3[@data-testid="lists-title"]'
    BOOK_NAME = '//h3[@class="tss-1a1lxt0-ellipsize MuiBox-root mui-0"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_list_name_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.LIST_NAME_BUTTON)))
        return element.text

    def get_book_name(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.BOOK_NAME)))
        return element.text

    def enter_delete_page(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LIST_NAME_BUTTON)))
        return element.click()
