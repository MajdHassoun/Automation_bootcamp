from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class ShoppingCart(BasePageApp):
    REMOVE_BUTTON_IN_CART_BACKPACK = (By.XPATH, '//button[@id = "remove-sauce-labs-backpack"]')
    REMOVE_BUTTON_IN_CART_T_SHIRT = (By.XPATH, '////button[@id = "remove-sauce-labs-bolt-t-shirt"]')
    REMOVE_BUTTON_IN_CART_BIKE_LIGHT = (By.XPATH, '//button[@id = "remove-sauce-labs-bike-light"]')
    CONTINUE_SHOPPING_IN_CART_BUTTON = (By.XPATH, '//button[@id = "continue-shopping"]')
    CHECKOUT_BUTTON_IN_CART = (By.XPATH, '//button[@class = "btn btn_action btn_medium checkout_button "]')
    ITEM_NAME_LINK_CLICK_IN_CART = (By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]')

    # ITEMS_CART = (By.XPATH, '//div[@class = "cart_list]')

    def __init__(self, driver):
        super().__init__(driver)
        self._remove_button_in_cart_backpack = self._driver.find_element(self.REMOVE_BUTTON_IN_CART_BACKPACK)
        self._remove_button_in_cart_t_shirt = self._driver.find_element(self.REMOVE_BUTTON_IN_CART_T_SHIRT)
        self._remove_button_in_cart_bike_light = self._driver.find_element(self.REMOVE_BUTTON_IN_CART_BIKE_LIGHT)
        self._continue_shopping_in_cart_button = self._driver.find_element(self.CONTINUE_SHOPPING_IN_CART_BUTTON)
        self._checkout_button_in_cart = self._driver.find_element(self.CHECKOUT_BUTTON_IN_CART)
        self._item_name_link_click_in_cart = self._driver.find_element(self.ITEM_NAME_LINK_CLICK_IN_CART)

    def remove_backpack_from_cart(self):
        self._remove_button_in_cart_backpack.click()

    def remove_t_shirt_from_cart(self):
        self._remove_button_in_cart_t_shirt.click()

    def remove_bike_light_from_cart(self):
        self._remove_button_in_cart_bike_light.click()

    def continue_shopping_button(self):
        self._continue_shopping_in_cart_button.click()

    def checkout_button(self):
        self._checkout_button_in_cart.click()

    def item_name_link_button_in_cart(self):
        self._item_name_link_click_in_cart.click()

    def count_items_in_cart(self):
        return len(self._driver.find_elements(By.XPATH, '//div[@class = "cart_list]'))

    def remove_and_check_items_flow(self):
        self.remove_bike_light_from_cart()
        return len(self._driver.find_elements(By.XPATH, '//div[@class = "cart_list]'))
