import time
import unittest

from selenium import webdriver

from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(2)

        


