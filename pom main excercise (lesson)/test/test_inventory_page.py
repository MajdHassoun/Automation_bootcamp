import time
import unittest

from selenium import webdriver

from infra.browser_wrapper import BrowserWrapper
from logic.inventory_page import InventoryPage
from logic.login_page import LoginPage


class TestInventoryPage(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login_flow("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    InventoryPage.add_backpack_to_cart()
