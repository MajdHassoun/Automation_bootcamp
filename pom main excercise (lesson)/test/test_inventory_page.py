import time
import unittest

from selenium import webdriver

# from infra.browser_wrapper import BrowserWrapper
from logic.inventory_page import InventoryPage
from logic.login_page import LoginPage
from logic.shopping_cart import ShoppingCart


class TestInventoryPage(unittest.TestCase):
    def test_stam_test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(2)
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.cart_button_inventory_click()
        time.sleep(2)
        cart_page = ShoppingCart(driver)
        print(cart_page.count_items_in_cart())
        time.sleep(2)

