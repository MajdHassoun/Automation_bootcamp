from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class DynamicContentPage(BasePage):
    REFRESH_BUTTON = '//a[text() = "click here"]'
    DYNAMIC_IMAGE = '(//div[@class = "large-2 columns"])[3]//img'
    DYNAMIC_TEXT = '(//div[@class = "large-10 columns"])[3]'

    def __init__(self, driver):
        super().__init__(driver)
        self._refresh_button = self._driver.find_element(By.XPATH, self.REFRESH_BUTTON)
        self._dynamic_image = self._driver.find_elements(By.XPATH, self.DYNAMIC_IMAGE)
        self._dynamic_text = self._driver.find_elements(By.XPATH, self.DYNAMIC_TEXT)

    def refresh_page(self):
        self._refresh_button.click()

    def get_dynamic_content_text(self):
        element = WebDriverWait(self._driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.DYNAMIC_TEXT)))
        return element.text

    def get_image_src(self):
        element = WebDriverWait(self._driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.DYNAMIC_IMAGE)))
        return element.get_attribute("src")
