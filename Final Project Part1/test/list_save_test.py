import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.delete_list_page import DeleteListPage
from logic.home_page import HomePage
from logic.first_sign_in_page import FirstSignInPage
from logic.lists_page import ListsPage
from logic.search_results_page import SearchResultsPage
from logic.second_sign_in_page import SecondSignInPage


class ListSaveTest(unittest.TestCase):
    def setUp(self):
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
        delete_list = DeleteListPage(self.driver)
        lists_page = ListsPage(self.driver)
        lists_page.enter_delete_page()
        delete_list.delete_list_flow()
        self.browser.close_browser()

    def test_make_and_save_to_list(self):
        results_page = SearchResultsPage(self.driver)
        results_page.add_create_list_flow(self.config["list_name"], self.config["list description"])
        lists_page = ListsPage(self.driver)
        results_page.navigate_to_lists_flow()
        self.assertEqual(lists_page.get_list_name_button(), self.config["list_name"])

    def test_check_if_book_in_list(self):
        results_page = SearchResultsPage(self.driver)
        results_page.add_create_list_flow(self.config["list_name"], self.config["list description"])
        lists_page = ListsPage(self.driver)
        results_page.navigate_to_lists_flow()
        self.assertEqual(lists_page.get_book_name(), self.config["book_name1"])
