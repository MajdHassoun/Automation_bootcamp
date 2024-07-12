from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class SecondSignInPage(BasePage):
    """
    SecondSignInPage class extends BasePage and provides methods for interacting with
    elements on the second sign-in page.
    """

    EMAIL_INPUT = '//input[@name = "signin.username"]'
    PASSWORD_INPUT = '//input[@name = "signin.password"]'
    SIGNIN_BUTTON = '//button[@id = "submitSignin"]'
    ERROR_MESSAGE = '//div[text()= "The email or password is invalid. Authentication failed."]'
    SIGN_IN_PAGE_TITLE = '//span[@title = "My Account in the European Data Center"]'

    def __init__(self, driver):
        """
        Initializes the SecondSignInPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def enter_email(self, email):
        """
        Enters the email into the email input field.

        Uses WebDriverWait to wait up to 15 seconds until the email input element is visible.

        :param email: The email to be entered into the email input field.
        """
        element = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT)))

        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        """
        Enters the password into the password input field.

        Uses WebDriverWait to wait up to 15 seconds until the password input element is visible.

        :param password: The password to be entered into the password input field.
        """
        password_input = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT))
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_signin_second_page(self):
        """
        Clicks the sign-in button on the second sign-in page.

        Uses WebDriverWait to wait up to 15 seconds until the sign-in button is clickable.
        """
        signin_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGNIN_BUTTON))
        )
        signin_button.click()

    def get_error_message(self):
        """
        Retrieves the error message displayed on the sign-in page.

        Uses WebDriverWait to wait up to 15 seconds until the error message element is visible.

        :return: The text content of the error message.
        """
        return WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE))
        ).text

    def get_sign_in_page_title(self):
        """
        Retrieves the title of the sign-in page.

        Uses WebDriverWait to wait up to 15 seconds until the page title element is visible.

        :return: The text content of the sign-in page title.
        """
        return WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.SIGN_IN_PAGE_TITLE))
        ).text

    def second_signin_flow(self, email, password):
        """
        Performs the flow to sign in with the provided email and password.

        Enters the email, password, and clicks the sign-in button.

        :param email: The email to be used for signing in.
        :param password: The password associated with the email.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin_second_page()
