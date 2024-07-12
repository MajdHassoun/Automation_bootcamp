import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.second_sign_in_page import SecondSignInPage


class SigninTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.home_page.refresh_page()
        self.home_page.click_accept_cookies()

    def tearDown(self):
        self.browser.close_browser()

    def test_valid_signin(self):
        self.home_page.click_sign_in()
        sign_in_page = FirstSignInPage(self.driver)
        sign_in_page.first_signin_flow(self.config["username"])
        sign_in_page2 = SecondSignInPage(self.driver)
        sign_in_page2.second_signin_flow(self.config["username"], self.config["password"])
        self.assertTrue(self.home_page.is_hello_user_message_displayed())

    def test_invalid_signin(self):
        self.home_page.click_sign_in()
        sign_in_page = FirstSignInPage(self.driver)
        sign_in_page.first_signin_flow(self.config["username"])
        sign_in_page2 = SecondSignInPage(self.driver)
        sign_in_page2.second_signin_flow(self.config["username"], self.config["wrong_password"])
        self.assertTrue(sign_in_page2.get_error_message())
