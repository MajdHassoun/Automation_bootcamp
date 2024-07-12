from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class BasePageApp(BasePage):
    """
    BasePageApp class encapsulates common functionalities for interacting with elements in the application header
    and profile sections. Inherits from BasePage.
    """
    HEADER_LOGO_LINK = '//header//img[@loading ="lazy"]'
    HEADER_HOME_BUTTON = '//a[@data-testid = "header-home-link"]'
    HEADER_LIBRARIES_BUTTON = '//a[@data-testid = "header-libraries-link"]'
    HEADER_LISTS_BUTTON = '//a[@data-testid = "header-lists-link"]'
    PROFILE_BUTTON = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_FAVORITE_LIBRARIES_BUTTON = '//li[@data-value = "favorite-libraries"]'
    PROFILE_LISTS_BUTTON = '//li[@data-value = "my-lists"]'
    PROFILE_SAVED_SEARCHES_BUTTON = '//li[@data-value = "saved-searches"]'

    def __init__(self, driver):
        """
        Initialize the BasePageApp class.

        :param driver: WebDriver instance.
        """
        super().__init__(driver)
        self._header_logo_link = self._driver.find_element(By.XPATH, self.HEADER_LOGO_LINK)

    def click_home_button(self):
        """
        Click the home button in the header.
        """
        header_home_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_HOME_BUTTON))
        )
        header_home_button.click()

    def click_header_libraries_button(self):
        """
        Click the libraries button in the header.
        """
        header_libraries_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_LIBRARIES_BUTTON))
        )
        header_libraries_button.click()

    def click_header_lists_button(self):
        """
        Click the lists button in the header.
        """
        lists_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HEADER_LISTS_BUTTON))
        )
        lists_button.click()

    def click_profile_button(self):
        """
        Click the profile button.
        """
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//h3[text() = "Create new list"]')))

        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_BUTTON)))

        element.click()

    def click_favorite_libraries_button(self):
        """
        Click the favorite libraries button in the profile section.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_FAVORITE_LIBRARIES_BUTTON)))
        element.click()

    def click_profile_lists_button(self):
        """
        Click the lists button in the profile section.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LISTS_BUTTON)))
        element.click()

    def click_saved_searches_button(self):
        """
        Click the saved searches button in the profile section.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_SAVED_SEARCHES_BUTTON)))
        element.click()

    def navigate_to_lists_flow(self):
        """
        Navigate to the lists section in the profile.
        """
        self.click_profile_button()
        self.click_profile_lists_button()

    def navigate_to_favorite_libraries_flow(self):
        """
        Navigate to the favorite libraries section in the profile.
        """
        self.click_profile_button()
        self.click_favorite_libraries_button()

    def navigate_to_favorite_libraries_for_delete_flow(self):
        """
        Navigate to the favorite libraries section in the profile for deletion.
        """
        # WebDriverWait(self._driver, 10).until(
        #     EC.text_to_be_present_in_element_attribute((By.XPATH,
        #                                                 '//div[@data-testid="library-favorite-button-section"]'),
        #                                                "aria-label", "Remove Kimico Ltd as a favorite library"))
        # WebDriverWait(self._driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//div[text() = "Kimico Ltd added to favorite libraries"]')))
        # time.sleep(2)
        self.click_profile_button()
        self.click_favorite_libraries_button()

    def navigate_to_saved_searches_flow(self):
        """
        Navigate to the saved searches section in the profile.
        """
        WebDriverWait(self._driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//h3[text()="Save your search"]')))
        self.click_profile_button()
        self.click_saved_searches_button()
