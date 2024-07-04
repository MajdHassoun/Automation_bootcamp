from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class InventoryPage(BasePageApp):
    ADD_TO_CART_BUTTON_BACKPACK = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BUTTON_BIKE_LIGHT = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    ADD_TO_CART_BUTTON_T_SHIRT = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    ITEM_NAME_BUTTON = '//div[contains(text(), "Sauce Labs Backpack")]'
    IMAGE_CLICK = '//a[@id="item_4_img_link"]//img'  # anan's method (its more stable)
    CART_BUTTON_INVENTORY =  '//a[@class="shopping_cart_link"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button_backpack = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_BACKPACK)
        self._add_to_cart_button_bike_light = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_BIKE_LIGHT)
        self._add_to_cart_button_t_shirt = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_T_SHIRT)
        self._item_name_button = self._driver.find_element(By.XPATH, self.ITEM_NAME_BUTTON)
        self._image_click = self._driver.find_element(By.XPATH, self.IMAGE_CLICK)
        self.cart_button_inventory = self._driver.find_element(By.XPATH, self.CART_BUTTON_INVENTORY)

    def add_backpack_to_cart(self):
        self._add_to_cart_button_backpack.click()

    def add_t_shirt_to_cart(self):
        self._add_to_cart_button_t_shirt.click()

    def add_bike_light_to_cart(self):
        self._add_to_cart_button_bike_light.click()

    def cart_button_inventory_click(self):
        self.cart_button_inventory.click()

    def item_name_button_click(self):
        self._item_name_button.click()

    def image_click(self):
        self._image_click.click()

    def add_two_items_flow(self):
        self._add_to_cart_button_bike_light.click()
        self._add_to_cart_button_t_shirt.click()

    def add_three_items_flow(self):
        self._add_to_cart_button_bike_light.click()
        self._add_to_cart_button_t_shirt.click()
        self._add_to_cart_button_backpack.click()
