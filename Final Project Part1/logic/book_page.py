from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class BookPage(BasePageApp):
    BOOK_NAME = '//h1[@class="MuiTypography-root MuiTypography-h3 mui-1v2s94n"]'
    BOOK_SUMMARY = '(//div[@class="tss-86eodb-lineClamp MuiBox-root mui-0"])[2]'
    BOOK_AVAILABILITY = '(//div//p[@data-testid="show-number-editions"])[1]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_book_name(self):
        book_name = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.BOOK_NAME))
        )
        return book_name.text

    def is_book_summary_displayed(self):
        book_summary = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.BOOK_SUMMARY))
        )
        return book_summary.is_displayed()

    def is_book_availability_displayed(self):
        book_availability = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.BOOK_AVAILABILITY))
        )
        return book_availability.is_displayed()
