from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from infra.base_page import BasePage


class DragAndDropPage(BasePage):
    SQUARE_LEFT = '//div[@id = "column-a"]'
    SQUARE_RIGHT = '//div[@id = "column-b"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._square_left = self._driver.find_element(By.XPATH, self.SQUARE_LEFT)
        self._square_right = self._driver.find_element(By.XPATH, self.SQUARE_RIGHT)

    def drag_and_drop_l_to_r(self):
        source_element = self._square_left
        target_element = self._square_right
        actions = ActionChains(self._driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    def drag_and_drop_r_to_l(self):
        source_element = self._square_right
        target_element = self._square_left
        actions = ActionChains(self._driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
