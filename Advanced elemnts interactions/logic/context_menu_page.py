from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class ContextMenuPage(BasePage):
    CLICKABLE_BOX = '//div[@id ="hot-spot"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._clickable_box = self._driver.find_element(By.XPATH, self.CLICKABLE_BOX)

    def click_on_the_box(self):
        action = ActionChains(self._driver)
        action.context_click(self._clickable_box).perform()

