import time
import unittest

from selenium import webdriver

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.inventory_page import InventoryPage
from logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def test_login(self):
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        inventory_page = InventoryPage(driver)
        time.sleep(2)

        


