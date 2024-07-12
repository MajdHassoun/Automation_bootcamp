from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class FirstSignInPage(BasePage):
    """
    FirstSignInPage class extends BasePage and provides methods for interacting with
    elements on the first sign-in page.
    """

    # XPaths for elements on the first sign-in page
    EMAIL_INPUT = '//input[@name = "emailField"]'
    CONTINUE_BUTTON = '//button[@type = "submit"]'
    PAGE_TITLE = '//h1[text()="Welcome to WorldCat.org"]'

    def __init__(self, driver):
        """
        Initializes the FirstSignInPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def enter_email(self, email):
        """
        Enters the email into the email input field.

        Uses WebDriverWait to wait up to 15 seconds until the email input field is visible.

        :param email: The email address to enter.
        """
        email_input = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT))
        )
        email_input.clear()
        email_input.send_keys(email)

    def click_continue(self):
        """
        Clicks the continue button.

        Uses WebDriverWait to wait up to 15 seconds until the continue button is clickable.
        """
        continue_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        )
        continue_button.click()

    def get_page_title(self):
        """
        Retrieves the title of the page.

        Uses WebDriverWait to wait up to 15 seconds until the page title element is visible.

        :return: The text of the page title element.
        """
        page_title = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))
        )
        return page_title.text

    def first_signin_flow(self, email):
        """
        Executes the flow for the first sign-in by entering the email and clicking continue.

        :param email: The email address to enter.
        """
        self.enter_email(email)
        self.click_continue()
