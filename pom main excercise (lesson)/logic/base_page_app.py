from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    CART_BUTTON = '//a[@class="shopping_cart_link"]'
    MENU_BUTTON = '//button[@id= "react-burger-menu-btn"]'
    ALL_ITEMS_MENU_BUTTON = '//a[@id= "inventory_sidebar_link"]'
    ABOUT_MENU_BUTTON = '//a[@id= "about_sidebar_link"]'
    LOGOUT_MENU_BUTTON = '//a[@id= "logout_sidebar_link"]'
    RESET_MENU_BUTTON = '//a[@id= "reset_sidebar_link"]'
    TWITTER_BUTTON = '//a[@data-test="social-twitter"]'
    FACEBOOK_BUTTON = '//a[@data-test="social-facebook"]'
    LINKEDIN_BUTTON = '//a[@data-test="social-linkedin"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
        self._all_items_menu_button = self._driver.find_element(By.XPATH, self.ALL_ITEMS_MENU_BUTTON)
        self._about_menu_button = self._driver.find_element(By.XPATH, self.ABOUT_MENU_BUTTON)
        self._logout_menu_button = self._driver.find_element(By.XPATH, self.LOGOUT_MENU_BUTTON)
        self._reset_menu_button = self._driver.find_element(By.XPATH, self.RESET_MENU_BUTTON)
        self._twitter_button = self._driver.find_element(By.XPATH, self.TWITTER_BUTTON)
        self._facebook_button = self._driver.find_element(By.XPATH, self.FACEBOOK_BUTTON)
        self._linkedin_button = self._driver.find_element(By.XPATH, self.LINKEDIN_BUTTON)

    def click_cart_button(self):
        self._cart_button.click()

    def click_menu_button(self):
        self._menu_button.click()

    def click_all_items_menu_button(self):
        self._all_items_menu_button.click()

    def click_about_menu_button(self):
        self._about_menu_button.click()

    def click_logout_menu_button(self):
        self._logout_menu_button.click()

    def click_reset_menu_button(self):
        self._reset_menu_button.click()

    def click_twitter_button(self):
        self._twitter_button.click()

    def click_facebook_button(self):
        self._facebook_button.click()

    def click_linkedin_button(self):
        self._linkedin_button.click()
