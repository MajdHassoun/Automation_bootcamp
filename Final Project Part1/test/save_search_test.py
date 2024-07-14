import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.saved_searches_page import SavedSearchesPage
from logic.search_results_page import SearchResultsPage
from logic.second_sign_in_page import SecondSignInPage
from logic.base_page_app import BasePageApp


class LibraryTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.base_page_app = BasePageApp(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.refresh_page()
        self.home_page.click_accept_cookies()
        self.home_page.click_sign_in()
        first_sign_in = FirstSignInPage(self.driver)
        first_sign_in.first_signin_flow(self.config["username"])
        second_sign_in = SecondSignInPage(self.driver)
        second_sign_in.second_signin_flow(self.config["username"], self.config["password"])
        self.results_page = SearchResultsPage(self.driver)
        self.saved_searches_page = SavedSearchesPage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_save_search(self):
        # Arrange
        self.home_page.search_book_flow(self.config["book_name1"])
        # Act
        self.results_page.click_save_search_button()
        self.results_page.click_confirm_save_search_button()
        self.base_page_app.navigate_to_saved_searches_flow()
        # Assert
        self.assertTrue(self.saved_searches_page.get_search_name())

    def test_delete_saved_search(self):
        self.base_page_app.navigate_to_saved_searches_flow()
        # Act
        self.saved_searches_page.click_saved_searches_checkbox()
        self.saved_searches_page.click_delete_search_button()
        # Assert
        self.assertTrue(self.saved_searches_page.get_no_saved_searches_message())
