from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def click_home_button(self):
        header_home_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_HOME_BUTTON))
        )
        header_home_button.click()

    def click_header_libraries_button(self):
        header_libraries_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_LIBRARIES_BUTTON))
        )
        header_libraries_button.click()

    def click_header_topics_button(self):
        topics_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_TOPICS_BUTTON))
        )
        topics_button.click()

    def click_header_lists_button(self):
        lists_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_LISTS_BUTTON))
        )
        lists_button.click()

    def click_header_about_button(self):
        about_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_ABOUT_BUTTON))
        )
        about_button.click()

    def click_header_for_librarians_button(self):
        for_librarians_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_FOR_LIBRARIANS_BUTTON))
        )
        for_librarians_button.click()

    def is_footer_logo_visible(self):
        footer_logo = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.FOOTER_LOGO))
        )

        return footer_logo.is_displayed()

    def click_profile_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//h3[text() = "Create new list"]')))

        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_BUTTON)))

        element.click()

    def click_favorite_libraries_button(self):
        element = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_FAVORITE_LIBRARIES_BUTTON)))
        element.click()

    def click_profile_lists_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LISTS_BUTTON)))
        element.click()

    def click_saved_searches_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_SAVED_SEARCHES_BUTTON)))
        element.click()

    def navigate_to_lists_flow(self):
        self.click_profile_button()
        self.click_profile_lists_button()

    def navigate_to_favorite_libraries_flow(self):
        # WebDriverWait(self._driver, 10).until(
        #     EC.text_to_be_present_in_element_attribute((By.XPATH,
        #                                                 '//button[@data-testid="library-favorite-icon-216413"]'),
        #                                                "aria-label", "Remove Kimico Ltd as a favorite library"))
        self.click_profile_button()
        self.click_favorite_libraries_button()

    def navigate_to_saved_searches_flow(self):
        self.click_profile_button()
        self.click_saved_searches_button()
