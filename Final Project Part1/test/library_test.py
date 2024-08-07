import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.favorite_libraries_page import FavoriteLibrariesPage
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.libraries_page import LibrariesPage
from logic.libraries_search_results_page import LibrariesSearchResultsPage
from logic.second_sign_in_page import SecondSignInPage
from logic.base_page_app import BasePageApp
import logging
from infra.logging_setup import logger_setup


class LibraryTest(unittest.TestCase):
    # Arrange
    def setUp(self):
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

    def tearDown(self):
        self.browser.close_browser()

    def test_find_and_favorite_library(self):
        """ This test searches for a library in the "Libraries" page and saves it as favorite"""
        logging.info("Test test_find_and_favorite_library STARTED")
        # Arrange
        libraries_page = LibrariesPage(self.driver)
        self.base_page_app.click_header_libraries_button()
        library_search_result_page = LibrariesSearchResultsPage(self.driver)
        libraries_page.libraries_search_flow(self.config["library_name"])
        # Act
        library_search_result_page.click_save_library_to_favorites_button()
        self.base_page_app.navigate_to_favorite_libraries_flow()
        favorite_libraries_page = FavoriteLibrariesPage(self.driver)
        library_name = favorite_libraries_page.get_favorite_library_name()
        # Assert
        self.assertEqual(library_name, self.config["library_name"])
        logging.info("Test test_find_and_favorite_library ENDED")

    def test_find_and_unfavorite_library(self):
        """ This test enters the "Libraries" page and unfavorite the saved as favorite library"""
        logging.info("Test test_find_and_unfavorite_library STARTED")
        # Arrange
        self.base_page_app.navigate_to_favorite_libraries_for_delete_flow()
        favorite_libraries_page = FavoriteLibrariesPage(self.driver)
        # Act
        favorite_libraries_page.remove_favorite_library_flow()
        # Assert
        self.assertTrue(favorite_libraries_page.get_no_libraries_message())
        logging.info("Test test_find_and_unfavorite_library ENDED")
