import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.delete_list_page import DeleteListPage
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.lists_page import ListsPage
from logic.search_results_page import SearchResultsPage
from logic.second_sign_in_page import SecondSignInPage
import logging
from infra.logging_setup import logger_setup


class ListDeleteTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.home_page.refresh_page()
        self.home_page.click_accept_cookies()
        self.home_page.click_sign_in()
        first_sign_in = FirstSignInPage(self.driver)
        first_sign_in.first_signin_flow(self.config["username"])
        second_sign_in = SecondSignInPage(self.driver)
        second_sign_in.second_signin_flow(self.config["username"], self.config["password"])
        self.home_page.search_book_flow(self.config["book_name1"])

    def tearDown(self):
        self.browser.close_browser()

    def test_delete_list(self):
        """ This test deletes a list that has been created from the "Lists" page """
        logging.info("Test test_delete_library STARTED")
        # Arrange
        results_page = SearchResultsPage(self.driver)
        results_page.add_create_list_flow(self.config["list_name"], self.config["list description"])
        lists_page = ListsPage(self.driver)
        results_page.navigate_to_lists_flow()
        lists_page.enter_delete_page()
        delete_list_page = DeleteListPage(self.driver)
        # Act
        delete_list_page.delete_list_flow()
        # Assert
        self.assertTrue(delete_list_page.get_no_lists_found_message())
        logging.info("Test test_delete_library ENDED")
