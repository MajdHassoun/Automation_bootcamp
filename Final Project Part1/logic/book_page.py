from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class BookPage(BasePageApp):
    BOOK_NAME = '//h1[@class="MuiTypography-root MuiTypography-h3 mui-1v2s94n"]'
    BOOK_SUMMARY = '(//div[@class="tss-86eodb-lineClamp MuiBox-root mui-0"])[2]'
    BOOK_AVAILABILITY = '(//div//p[@data-testid="show-number-editions"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._book_name = self._driver.find_element(By.XPATH, self.BOOK_NAME)
        self._book_summary = self._driver.find_element(By.XPATH, self.BOOK_SUMMARY)
        self._book_availability = self._driver.find_element(By.XPATH, self.BOOK_AVAILABILITY)

    def get_book_name(self):
        return self._book_name.text

    def get_book_summary(self):
        return self._book_summary.text

    def get_book_availability(self):
        return self._book_availability.text
