from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class SearchResultsPage(BasePageApp):
    RESULTS_LIST = '//h2//a[@class = "MuiTypography-root' \
                   ' MuiTypography-inherit MuiLink-root MuiLink-underlineAlways' \
                   ' tss-1cxpzkn-root mui-3nwq8n"]'
    ITEM_TYPE = '//span[@class="tss-14id4vs-container MuiBox-root mui-0"]'
    ADD_ITEM_TO_LIST = '//span[@class="MuiButton-icon MuiButton-startIcon' \
                       ' MuiButton-iconSizeMedium mui-6xugel"]'
    CREATE_LIST_NAME_INPUT = '//input[@id="list-name"]'
    LIST_DESCRIPTION_INPUT = '//textarea[@name="listDescription"]'
    CREATE_LIST_BUTTON = '//button[@data-testid="create-list-dialog-create-button"]'
    SAVE_SEARCH_BUTTON = '//button[@data-testid="save-search-button"]'
    CONFIRM_SAVE_SEARCH_BUTTON = '//button[@data-testid="save-search-dialog-create-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._results_list = self._driver.find_elements(By.XPATH, self.RESULTS_LIST)
        self._item_type = self._driver.find_elements(By.XPATH, self.ITEM_TYPE)
        self._add_item_to_list = self._driver.find_element(By.XPATH, self.ADD_ITEM_TO_LIST)
        self._save_search_button = self._driver.find_element(By.XPATH, self.SAVE_SEARCH_BUTTON)

    def click_first_result(self):
        """Clicks the first result in the results list."""
        self._results_list[0].click()

    def return_first_result_name(self):
        return self._results_list[0].text

    def get_item_type_text(self):
        """Returns the text of the item type element."""
        return self._item_type[0].text

    def click_add_item_to_list(self):
        """Clicks the 'add item to list' button."""
        self._add_item_to_list.click()

    def enter_list_name(self, name):
        """Enters a name into the 'create list name' input field."""
        create_list_name_input = self._driver.find_element(By.XPATH, self.CREATE_LIST_NAME_INPUT)
        create_list_name_input.clear()
        create_list_name_input.send_keys(name)

    def enter_list_description(self, description):
        """Enters a description into the 'list description' input field."""
        list_description_input = self._driver.find_element(By.XPATH, self.LIST_DESCRIPTION_INPUT)
        list_description_input.clear()
        list_description_input.send_keys(description)

    def click_create_list_button(self):
        """Clicks the 'create list' button."""
        create_list_button = self._driver.find_element(By.XPATH, self.CREATE_LIST_BUTTON)
        create_list_button.click()

    def create_list_flow(self, list_name, list_description):
        """Flow function to create a list starting from clicking the add item to list button."""
        self.click_add_item_to_list()
        self.enter_list_name(list_name)
        self.enter_list_description(list_description)
        self.click_create_list_button()

    def click_save_search_button(self):
        self._save_search_button.click()

    def click_confirm_save_search_button(self):
        confirm_save_search_button = self._driver.find_element(By.XPATH, self.CONFIRM_SAVE_SEARCH_BUTTON)
        confirm_save_search_button.click()
