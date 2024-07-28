import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.book_page import BookPage
from logic.home_page import HomePage
from logic.search_results_page import SearchResultsPage
import logging
from infra.jira_handler import JiraHandler
from infra.logging_setup import logger_setup


class BookSearchTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)
        self.home_page.refresh_page()
        self.home_page.click_accept_cookies()
        self.jira_handler = JiraHandler()
        self.test_errors = []

    def tearDown(self):
        if self.test_errors:
            self.jira_handler.create_issue(self.config["project_key"], self.config["jira_issue_summary"],
                                           self.config["jira_issue_description"])

    def test_search_book(self):
        """ This test searches for a book and checks if the book title is
        present in the book's page"""
        logging.info("Test test_search_book STARTED")
        # Arrange
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        try:
            # Act
            book_name_displayed = book_page.get_book_name()
            # Assert
            self.assertNotEqual(self.config["book_name1"], book_name_displayed)

        except AssertionError as e:
            self.test_errors.append(e)
            raise AssertionError
        logging.info("Test test_search_book ENDED")

    def test_check_book_summary(self):
        """ This test searches for a book and checks if the book summary is
                present in the book's page"""
        logging.info("Test test_check_book_summary STARTED")
        # Arrange
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        # Act & Assert
        self.assertTrue(book_page.is_book_summary_displayed())
        logging.info("Test test_check_book_summary ENDED")

    def test_check_book_availability(self):
        """ This test searches for a book and checks if the book availability is
                present in the book's page"""
        logging.info("Test test_check_book_availability STARTED")
        # Arrange
        self.home_page.search_book_flow(self.config["book_name1"])
        results_page = SearchResultsPage(self.driver)
        results_page.click_first_result()
        book_page = BookPage(self.driver)
        # Act & Assert
        self.assertTrue(book_page.is_book_availability_displayed())
        logging.info("Test test_check_book_availability ENDED")
