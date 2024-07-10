import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.second_sign_in_page import SecondSignInPage


class ValidRegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_valid_signin(self):
        self.home_page.click_on_cookies()
        time.sleep(3)
        self.home_page.click_on_sign_in_button()
        time.sleep(1)
        sign_in_page = FirstSignInPage(self.driver)
        sign_in_page.enter_email(self.config["username"])
        sign_in_page.click_continue()
        time.sleep(7)
        sign_in_page2 = SecondSignInPage(self.driver)
        sign_in_page2.second_signin_flow(self.config["username"], self.config["password"])
        time.sleep(10)
        self.assertTrue(self.home_page.is_hello_user_message_visible())

    def test_invalid_signin(self):
        self.home_page.click_on_cookies()
        time.sleep(3)
        self.home_page.click_on_sign_in_button()
        time.sleep(1)
        sign_in_page = FirstSignInPage(self.driver)
        sign_in_page.enter_email(self.config["username"])
        sign_in_page.click_continue()
        time.sleep(2)
        sign_in_page2 = SecondSignInPage(self.driver)
        time.sleep(4)
        sign_in_page2.second_signin_flow(self.config["username"], self.config["wrong_password"])
        self.assertTrue(sign_in_page2.error_message_display())

