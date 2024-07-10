from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class LibrariesPage(BasePageApp):
    LIBRARIES_SEARCH_BAR = '//input[@placeholder="Type a library name"]'
    LIBRARIES_DISTANCE = '//p[@class="MuiTypography-root MuiTypography-body2 mui-ar2wnm"]'
    LIBRARIES_TITLE_PAGE = '//h1[text()="Libraries"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._libraries_search_bar = self._driver.find_element(By.XPATH, self.LIBRARIES_SEARCH_BAR)
        self._libraries_distance = self._driver.find_elements(By.XPATH, self.LIBRARIES_DISTANCE)
        self._libraries_title_page = self._driver.find_element(By.XPATH, self.LIBRARIES_TITLE_PAGE)

    def enter_library_name(self, name):
        self._libraries_search_bar.clear()
        self._libraries_search_bar.send_keys(name)

    def get_libraries_distance(self):
        return self._libraries_distance

    def get_libraries_title_page(self):
        return self._libraries_title_page.text

    def check_results_distance(self):
        distances_list = []
        old_list = [dis.text for dis in self.get_libraries_distance()]
        for distance in old_list:
            split_result = distance.split()
            distance_number = float(split_result[0])
            distances_list.append(distance_number)

