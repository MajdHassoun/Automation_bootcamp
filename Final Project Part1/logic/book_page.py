from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class BookPage(BasePageApp):
    """
    BookPage class extends BasePageApp and provides methods for interacting with
    elements on the book details page.
    """

    # XPaths for elements on the book details page
    BOOK_NAME = '//h1[@class="MuiTypography-root MuiTypography-h3 mui-1v2s94n"]'
    BOOK_SUMMARY = '(//div[@class="tss-86eodb-lineClamp MuiBox-root mui-0"])[2]'
    BOOK_AVAILABILITY = '(//div//p[@data-testid="show-number-editions"])[1]'

    def __init__(self, driver):
        """
        Initializes the BookPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def get_book_name(self):
        """
        Retrieves the name of the book.

        Uses WebDriverWait to wait up to 15 seconds until the book name element is present.

        :return: The text of the book name element.
        """
        book_name = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.BOOK_NAME))
        )
        return book_name.text

    def is_book_summary_displayed(self):
        """
        Checks if the book summary is displayed.

        Uses WebDriverWait to wait up to 15 seconds until the book summary element is visible.

        :return: True if the book summary is visible, False otherwise.
        """
        book_summary = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.BOOK_SUMMARY))
        )
        return book_summary.is_displayed()

    def is_book_availability_displayed(self):
        """
        Checks if the book availability information is displayed.

        Uses WebDriverWait to wait up to 15 seconds until the book availability element is visible.

        :return: True if the book availability is visible, False otherwise.
        """
        book_availability = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.BOOK_AVAILABILITY))
        )
        return book_availability.is_displayed()
