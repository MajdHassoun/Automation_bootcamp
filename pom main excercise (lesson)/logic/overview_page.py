from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class OverviewPage(BasePageApp):
    CANCEL_ORDER_BUTTON = (By.XPATH, '//button[@class = "btn btn_secondary back btn_medium cart_cancel_link"]')
    FINISH_ORDER_BUTTON = (By.XPATH, '//button[@class = "btn btn_action btn_medium cart_button"]')
    SUMMARY_INFO = (By.XPATH, '//div[@class = "summary_info"]')
    ITEM_NAME_LINK_OVERVIEW_PAGE = (By.XPATH, '//a[@id="item_1_title_link"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._cancel_order_button = self._driver.find_element(self.CANCEL_ORDER_BUTTON)
        self._finish_order_button = self._driver.find_element(self.FINISH_ORDER_BUTTON)
        self._summary_info = self._driver.find_element(self.SUMMARY_INFO)
        self._item_name_link_overview_page = self._driver.find_element(self.ITEM_NAME_LINK_OVERVIEW_PAGE)

    def click_cancel_order_button(self):
        self._cancel_order_button.click()

    def click_finish_order_button(self):
        self._finish_order_button.click()

    def get_summary_info(self):
        return self._summary_info.text

    def click_item_name_link_overview_page(self):
        self._item_name_link_overview_page.click()
