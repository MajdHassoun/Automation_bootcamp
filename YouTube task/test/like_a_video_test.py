import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.base_page_app import BasePageApp
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
        self.initial_page.click_sign_in_button()
        self.sign_in_page = SignInPage(self.driver)
        self.sign_in_page.sign_in(self.config["username"], self.config["password"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_signin_search(self):
        self.home_page.search("Cristiano Ronaldo")
        time.sleep(0.3)
        results_page = ResultsPage(self.driver)
        search_result = results_page.get_first_result_title()
        time.sleep(1)
        self.assertIn("Cristiano Ronaldo", search_result)
