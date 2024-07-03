from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class ItemPage(BasePageApp):
    REMOVE_BUTTON_ITEM_PAGE = (By.XPATH, '//button[@id = "remove"]')
    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, '//button[@id = "back-to-products"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._remove_button_item_page = driver.find_element(self.REMOVE_BUTTON_ITEM_PAGE)
        self._back_to_products_button = driver.find_element(self.BACK_TO_PRODUCTS_BUTTON)

    def remove_remove_button_item_page(self):
        self._remove_button_item_page.click()

    def back_to_products_button(self):
        self._back_to_products_button.click()

    