from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class DynamicControlsPage(BasePage):
    CHECKBOX = '//input[@type="checkbox"]'
    ADD_REMOVE_BUTTON = '//button[@onclick="swapCheckbox()"]'

    INPUT = '//input[@type="text"]'
    DISABLE_ENABLE_BUTTON = '//button[@onclick="swapInput()"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._checkbox = self._driver.find_element(By.XPATH, self.CHECKBOX)
        self._input = self._driver.find_element(By.XPATH, self.INPUT)

    def click_on_checkbox(self):
        self._checkbox.click()

    def get_add_remove_button_text(self):
        return self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).text

    def click_on_remove_button(self):
        if self.get_add_remove_button_text() == "Remove":
            self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_REMOVE_BUTTON)))

    def click_on_add_button(self):
        if self.get_add_remove_button_text() == "Add":
            self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_REMOVE_BUTTON)))
        # Refresh the checkbox element after the button click
        self._checkbox = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CHECKBOX)))

    def click_on_checkbox_forced(self):
        self.click_on_add_button()
        self.click_on_checkbox()

    # -------------------------------------------------------------------

    def type_in_input(self, text):
        self._input.clear()
        self._input.send_keys(text)

    def get_enable_disable_button_text(self):
        return self._driver.find_element(By.XPATH, self.DISABLE_ENABLE_BUTTON).text

    def click_on_enable_button(self):
        if self.get_enable_disable_button_text() == "Enable":
            self._driver.find_element(By.XPATH, self.DISABLE_ENABLE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.DISABLE_ENABLE_BUTTON)))

    def click_on_disable_button(self):
        if self.get_enable_disable_button_text() == "Disable":
            self._driver.find_element(By.XPATH, self.DISABLE_ENABLE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.DISABLE_ENABLE_BUTTON)))

    def type_in_input_forced(self, text):
        self.click_on_enable_button()
        self.type_in_input(text)
