from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class BasePageApp(BasePage):
    HEADER_LOGO_LINK = '//header//img[@loading ="lazy"]'
    HEADER_HOME_BUTTON = '//a[@data-testid = "header-home-link"]'
    HEADER_LIBRARIES_BUTTON = '//a[@data-testid = "header-libraries-link"]'
    HEADER_TOPICS_BUTTON = '//a[@data-testid = "header-topics-link"]'
    HEADER_LISTS_BUTTON = '//a[@data-testid = "header-lists-link"]'
    HEADER_ABOUT_BUTTON = '//a[@data-testid = "header-about-link"]'
    HEADER_FOR_LIBRARIANS_BUTTON = '//a[@data-testid = "header-for-librarians-link"]'
    FOOTER_LOGO = '//img[@data-testid = "worldcat-logo-white"]'
    PROFILE_BUTTON = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_FAVORITE_LIBRARIES_BUTTON = '//li[@data-value = "favorite-libraries"]'
    PROFILE_LISTS_BUTTON = '//li[@data-value = "my-lists"]'
    PROFILE_SAVED_SEARCHES_BUTTON = '//li[@data-value = "saved-searches"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._header_logo_link = self._driver.find_element(By.XPATH, self.HEADER_LOGO_LINK)
        self._header_home_button = self._driver.find_element(By.XPATH, self.HEADER_HOME_BUTTON)
        self._header_libraries_button = self._driver.find_element(By.XPATH, self.HEADER_LIBRARIES_BUTTON)
        self._header_topics_button = self._driver.find_element(By.XPATH, self.HEADER_TOPICS_BUTTON)
        self._header_lists_button = self._driver.find_element(By.XPATH, self.HEADER_LISTS_BUTTON)
        self._header_about_button = self._driver.find_element(By.XPATH, self.HEADER_ABOUT_BUTTON)
        self._header_for_librarians_button = self._driver.find_element(By.XPATH, self.HEADER_FOR_LIBRARIANS_BUTTON)
        self._footer_logo = self._driver.find_element(By.XPATH, self.FOOTER_LOGO)

    def click_home_button(self):
        self._header_home_button.click()

    def click_libraries_button(self):
        self._header_libraries_button.click()

    def click_topics_button(self):
        self._header_topics_button.click()

    def click_lists_button(self):
        self._header_lists_button.click()

    def click_about_button(self):
        self._header_about_button.click()

    def click_for_librarians_button(self):
        self._header_for_librarians_button.click()

    def is_footer_logo_visible(self):
        return self._footer_logo.is_displayed()

    def click_profile_button(self):
        profile_button = self._driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        profile_button.click()

    def click_favorite_libraries_button(self):
        profile_favorite_libraries_button = self._driver.find_element(By.XPATH,
                                                                      self.PROFILE_FAVORITE_LIBRARIES_BUTTON)
        profile_favorite_libraries_button.click()

    def click_profile_lists_button(self):
        profile_lists_button = self._driver.find_element(By.XPATH, self.PROFILE_LISTS_BUTTON)
        profile_lists_button.click()

    def click_saved_searches_button(self):
        profile_saved_searches_button = self._driver.find_element(By.XPATH, self.PROFILE_SAVED_SEARCHES_BUTTON)
        profile_saved_searches_button.click()

    # def view_all_subscriptions(self):
    #     element = WebDriverWait(self._driver, 15).until(
    #         EC.presence_of_element_located((By.XPATH, self.ALL_SUBSCRIPTION_BUTTON)))
    #     element.click()
    #     element.click()
