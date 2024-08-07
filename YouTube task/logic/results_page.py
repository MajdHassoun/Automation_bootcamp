from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class ResultsPage(BasePageApp):
    RESULTS_LIST = '//h3[@class = "title-and-badge style-scope ytd-video-renderer"]'
    FIRST_RESULT = '(//h3[@class = "title-and-badge style-scope ytd-video-renderer"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._results_list = self._driver.find_elements(By.XPATH, self.RESULTS_LIST)
        self._first_result = self._driver.find_element(By.XPATH, self.FIRST_RESULT)

    def get_results(self):
        """Returns a list of titles of the search results."""
        return [result.text for result in self._results_list]

    def get_first_result_title(self):
        """Returns the title of the first search result."""
        element = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.FIRST_RESULT)))
        return element.text
