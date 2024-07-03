from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    CART_BUTTON = (By.XPATH, '//a[@class="shopping_cart_link"]')
    MENU_BUTTON = (By.XPATH, '//button[@id= "react-burger-menu-btn"]')
    ALL_ITEMS_MENU_BUTTON = (By.XPATH, '//a[@id= "inventory_sidebar_link"]')
    ABOUT_MENU_BUTTON = (By.XPATH, '//a[@id= "about_sidebar_link"]')
    LOGOUT_MENU_BUTTON = (By.XPATH, '//a[@id= "logout_sidebar_link"]')
    RESET_MENU_BUTTON = (By.XPATH, '//a[@id= "reset_sidebar_link"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._cart_button = self._driver.find_element(self.CART_BUTTON)
        self._menu_button = self._driver.find_element(self.MENU_BUTTON)
