import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.base_page_app import BasePageApp
from logic.before_signin_home_page import BeforeSigninHomePage
from logic.home_page import HomePage


class ValidRegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = BeforeSigninHomePage(self.driver)

    def test_search(self):
        hp = BeforeSigninHomePage(self.driver)
        hp.enter_search_text("messi")
        time.sleep(1)
        self.driver.quit()
