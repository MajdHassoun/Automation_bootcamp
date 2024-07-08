from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class SubscriptionsPage(BasePageApp):
    SUBSCRIBED_TO_LIST = '//yt-formatted-string[@class ="style-scope ytd-channel-name"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._subscribed_to_list = self._driver.find_elements(By.XPATH, self.SUBSCRIBED_TO_LIST)

    def get_channels_name(self):
        return self._subscribed_to_list.text
