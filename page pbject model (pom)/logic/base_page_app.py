from infra.base_page import BasePage
from selenium.webdriver.common.by import By


class BasePageApp(BasePage):
    MAKE_APPOINTMENT_BUTTON = (By.XPATH, '//a[@id="btn-make-appointment"]')
    FACEBOOK_BUTTON = (By, '')
    TWITTER_BUTTON = (By, '')
    GLOBE_BUTTON = (By, '')
    INFO_EMAIL_BUTTON = (By, '')
    MAIN_BANNER = (By, 'erefe')
    SUB_BANNER = (By, '')


    def __init__(self, driver):
        super().__init__(driver)
        self._make_appointment_button = self._driver.find_element(self.MAKE_APPOINTMENT_BUTTON)
        #same for the rest
    def get_main_banner(self):
        return self.MAIN_BANNER.text
#more funcs to click and return headers