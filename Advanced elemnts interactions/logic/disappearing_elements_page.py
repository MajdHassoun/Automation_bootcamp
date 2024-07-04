from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class DisappearingElementsPage(BasePage):
    HOME_BUTTON = '//a[text() = "Home"]'
    ABOUT_BUTTON = '//a[text() = "About"]'
    CONTACT_US_BUTTON = '//a[text() = "Contact Us"]'
    PORTFOLIO_BUTTON = '//a[text() = "Portfolio"]'
    NOT_FOUND_MESSAGE = '//h1[text() = "Not Found"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._home_button = self._driver.find_element(By.XPATH, self.HOME_BUTTON)
        self._about_button = self._driver.find_element(By.XPATH, self.ABOUT_BUTTON)
        self._contact_us_button = self._driver.find_element(By.XPATH, self.CONTACT_US_BUTTON)
        self._portfolio_button = self._driver.find_element(By.XPATH, self.PORTFOLIO_BUTTON)

    def click_home_button(self):
        self._home_button.click()

    def click_about_button(self):
        self._about_button.click()
        not_found_message = self._driver.find_element(By.XPATH, self.NOT_FOUND_MESSAGE)
        print(not_found_message.is_displayed())

    def click_contact_us_button(self):
        self._contact_us_button.click()
        not_found_message = self._driver.find_element(By.XPATH, self.NOT_FOUND_MESSAGE)
        print(not_found_message.is_displayed())

    def click_portfolio_button(self):
        self._portfolio_button.click()
        not_found_message = self._driver.find_element(By.XPATH, self.NOT_FOUND_MESSAGE)
        print(not_found_message.is_displayed())
