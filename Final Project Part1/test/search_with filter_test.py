import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.search_results_page import SearchResultsPage
from logic.second_sign_in_page import SecondSignInPage
from logic.base_page_app import BasePageApp


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.base_page_app = BasePageApp(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.click_accept_cookies()
        self.home_page.click_sign_in()
        first_sign_in = FirstSignInPage(self.driver)
        first_sign_in.first_signin_flow(self.config["username"])
        second_sign_in = SecondSignInPage(self.driver)
        second_sign_in.second_signin_flow(self.config["username"], self.config["password"])
        self.results_page = SearchResultsPage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    # !!!!! supposed to be a test but there is a bug in the website !!!!! #
