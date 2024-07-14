from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp
from logic.utils import Utils


class LibrariesPage(BasePageApp):
    LIBRARIES_SEARCH_BAR = '//input[@placeholder="Type a library name"]'
    LIBRARIES_SEARCH_BUTTON = '//button[@data-testid="small-searchbox-search-button"]'
    LIBRARIES_DISTANCE = '//p[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    LIBRARIES_TITLE_PAGE = '//h1[text()="Libraries"]'

    def __init__(self, driver):
        """
        Initializes the LibrariesPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def enter_library_name(self, name):
        """
        Enters a library name into the search bar.

        Uses WebDriverWait to wait up to 15 seconds until the search bar is visible.

        :param name: The name of the library to search for.
        """
        library_search_bar = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARIES_SEARCH_BAR)))
        library_search_bar.clear()
        library_search_bar.send_keys(name)

    def click_search_button(self):
        """
        Clicks the search button.

        Uses WebDriverWait to wait up to 15 seconds until the search button is clickable.
        """
        libraries_search_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.LIBRARIES_SEARCH_BUTTON))
        )
        libraries_search_button.click()

    def get_libraries_distance(self):
        """
        Retrieves the distances of the libraries displayed.

        Uses WebDriverWait to wait up to 15 seconds until the distance elements are visible.

        :return: A list of elements representing the distances of the libraries.
        """
        libraries_distance = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.LIBRARIES_DISTANCE)))
        return libraries_distance

    def get_libraries_title_page(self):
        """
        Checks if the libraries title page is displayed.

        Uses WebDriverWait to wait up to 10 seconds until the title element is visible.

        :return: True if the title page is visible, False otherwise.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARIES_TITLE_PAGE)))
        return element.is_displayed()

    def check_results_distance(self):
        """
        Checks if the smallest distance is the first that is being displayed.


        :return: True if the minimum distance is the smallest, False otherwise.
        """
        strings_list = self.get_libraries_distance()
        distances_list = Utils.return_distance_from_string(strings_list)
        minimum_distance = distances_list[0]
        smallest_list_distance = min(distances_list)
        print(minimum_distance, smallest_list_distance)
        if minimum_distance == smallest_list_distance:
            return True

    def libraries_search_flow(self, name):
        """
        Executes the flow to search for a library by entering the library name and clicking the search button.

        :param name: The name of the library to search for.
        """
        self.enter_library_name(name)
        self.click_search_button()
