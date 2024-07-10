from logic.base_page_app import BasePageApp


class ListsPage(BasePageApp):
    LIST_NAME_BUTTON = '//h3[@data-testid="lists-title"]'
    BOOK_NAME = '//h3[@class="tss-1a1lxt0-ellipsize MuiBox-root mui-0"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._list_name_button = self._driver.find_element(By.XPATH, self.LIST_NAME_BUTTON)
        self._book_name = self._driver.find_element(By.XPATH, self.BOOK_NAME)

    def get_list_name_button(self):
        return self._list_name_button.click()

    def get_book_name(self):
        return self._book_name.is_displayed()
    
