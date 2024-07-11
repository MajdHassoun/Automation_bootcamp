import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.book_page import BookPage
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.search_results_page import SearchResultsPage
from logic.second_sign_in_page import SecondSignInPage


class BookSearchTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.home_page.click_accept_cookies()
        self.home_page.click_sign_in()
        first_sign_in = FirstSignInPage(self.driver)
        first_sign_in.first_signin_flow(self.config["username"])
        second_sign_in = SecondSignInPage(self.driver)
        second_sign_in.second_signin_flow(self.config["username"], self.config["password"])

    def tearDown(self):
        self.browser.close_browser()

    def test_search_book_with_signin(self):
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        # Act
        book_name_displayed = book_page.get_book_name()
        # Assert
        self.assertEqual(self.config["book_name1"], book_name_displayed)

    def test_check_book_summary_with_signin(self):
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        # Act
        # Assert
        self.assertTrue(book_page.is_book_summary_displayed())

    def test_check_book_availability_with_signin(self):
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        # Act
        # Assert
        self.assertTrue(book_page.is_book_availability_displayed())
