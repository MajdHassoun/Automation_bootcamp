from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class LibrariesPage(BasePageApp):
    LIBRARIES_SEARCH_BAR = '//input[@placeholder="Type a library name"]'
    LIBRARIES_SEARCH_BUTTON = '//button[@data-testid="small-searchbox-search-button"]'
    LIBRARIES_DISTANCE = '//p[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    LIBRARIES_TITLE_PAGE = '//h1[text()="Libraries"]'

    def __init__(self, driver):
        super().__init__(driver)

    def enter_library_name(self, name):
        library_search_bar = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARIES_SEARCH_BAR)))
        library_search_bar.clear()
        library_search_bar.send_keys(name)

    def click_search_button(self):
        libraries_search_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.LIBRARIES_SEARCH_BUTTON))
        )
        libraries_search_button.click()

    def get_libraries_distance(self):
        libraries_distance = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.LIBRARIES_DISTANCE)))
        return libraries_distance

    def get_libraries_title_page(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LIBRARIES_TITLE_PAGE)))
        return element.is_displayed()

    def check_results_distance(self):
        distances_list = []
        old_list = [dis.text for dis in self.get_libraries_distance()]
        for distance in old_list:
            split_result = distance.split()
            distance_number = float(split_result[0])
            distances_list.append(distance_number)
        minimum_distance = distances_list[0]
        smallest_list_distance = min(distances_list)
        print(minimum_distance, smallest_list_distance)
        if minimum_distance == smallest_list_distance:
            return True

    def libraries_search_flow(self, name):
        self.enter_library_name(name)
        self.click_search_button()
