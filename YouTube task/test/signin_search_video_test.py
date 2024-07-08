import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.before_signin_home_page import BeforeSigninHomePage
from logic.home_page import HomePage
from logic.results_page import ResultsPage
from logic.sign_in_page import SignInPage


class ValidRegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.initial_page = BeforeSigninHomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_signin_search(self):
        self.initial_page.click_sign_in_button()
        time.sleep(0.3)
        sign_in_page = SignInPage(self.driver)
        sign_in_page.enter_email_phone(self.config["username"])
        sign_in_page.click_next_button()
        sign_in_page.enter_password(self.config["password"])
        time.sleep(5)
        sign_in_page.click_next_button()
        time.sleep(5)
        home_page = HomePage(self.driver)
        home_page.search("Cristiano Ronaldo")
        time.sleep(5)
        results_page = ResultsPage(self.driver)
        search_result = results_page.get_first_result_title()
        time.sleep(1)
        self.assertIn("Cristiano Ronaldo", search_result)
