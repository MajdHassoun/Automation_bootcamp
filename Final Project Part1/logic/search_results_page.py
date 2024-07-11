from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    PAGE_RESULT_TITLE = '//h2[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_first_result(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.RESULTS_LIST)))
        element[0].click()

    def return_first_result_name(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.RESULTS_LIST)))
        return element[0].text

    def get_item_type_text(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ITEM_TYPE)))
        return element[0].text

    def click_add_item_to_list(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_ITEM_TO_LIST)))
        element.click()

    def enter_list_name(self, name):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CREATE_LIST_NAME_INPUT)))
        element.clear()
        element.send_keys(name)

    def enter_list_description(self, description):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.LIST_DESCRIPTION_INPUT)))
        element.clear()
        element.send_keys(description)

    def click_create_list_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_LIST_BUTTON)))
        element.click()
        # time.sleep(3)

    def create_list_flow(self, list_name, list_description):
        """Flow function to create a list starting from clicking the add item to list button."""
        self.click_add_item_to_list()
        self.enter_list_name(list_name)
        self.enter_list_description(list_description)
        self.click_create_list_button()

    def click_save_search_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_SEARCH_BUTTON)))
        element.click()

    def click_confirm_save_search_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_SAVE_SEARCH_BUTTON)))
        element.click()

    def add_create_list_flow(self, list_name, list_description):
        self.click_add_item_to_list()
        self.enter_list_name(list_name)
        self.enter_list_description(list_description)
        self.click_create_list_button()
