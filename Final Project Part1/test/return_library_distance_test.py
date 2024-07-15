import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.libraries_page import LibrariesPage
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

    def tearDown(self):
        self.browser.close_browser()

    def test_return_smallest_distance(self):
        """This test checks if the showed libraries are sorted according to the distance from the
        user's location """
        logging.info("Test test_return_smallest_distance STARTED")
        # Arrange
        libraries_page = LibrariesPage(self.driver)
        self.base_page_app.click_header_libraries_button()
        time.sleep(8)  # for presentation
        # Act & Assert
        self.assertTrue(libraries_page.check_results_distance())
        logging.info("Test test_return_smallest_distance COMPLETED \n \n")
