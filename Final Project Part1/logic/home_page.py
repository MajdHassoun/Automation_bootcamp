from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class HomePage(BasePage):
    SIGN_IN_BUTTON = '//a[text() = "Sign in"]'
    COOKIES_BUTTON = '//div[@class="banner-actions-container"]//button[text() = "Accept all cookies"]'
    HOME_PAGE_SEARCH_BAR = '//input[@id ="home-page-search-box"]'
    SEARCH_BUTTON_HOME_BAR = '//button[@data-testid ="search-button"]'
    HELLO_USER_MESSAGE = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_BUTTON = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_FAVORITE_LIBRARIES_BUTTON = '//li[@data-value = "favorite-libraries"]'
    PROFILE_LISTS_BUTTON = '//li[@data-value = "my-lists"]'
    PROFILE_SAVED_SEARCHES_BUTTON = '//li[@data-value = "saved-searches"]'
    FILTER_BUTTON = '//button[@aria-label="Advanced Search"]'
    FORMAT_FILTER_DROPBOX_BUTTON = '//div[@aria-labelledby="format-select"]'
    MUSIC_CD_DROPBOX_OPTION = '//li[@data-testid="format-select-music-cd"]'
    QUIT_DROPBOX_BUTTON = '//div[@class="MuiDialogContent-root tss-2a6ark-content mui-1ty026z"]'
    CONFIRM_SEARCH_BUTTON = '//button[@data-testid="advanced-search-search"]'

    def __init__(self, driver):
        """
        Initializes the HomePage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def click_sign_in(self):
        """
        Clicks the sign-in button.

        Uses WebDriverWait to wait up to 15 seconds until the sign-in button is clickable.
        """
        sign_in_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGN_IN_BUTTON))
        )
        sign_in_button.click()

    def click_accept_cookies(self):
        """
        Clicks the accept cookies button.

        Uses WebDriverWait to wait up to 15 seconds until the accept cookies button is clickable.
        """
        cookies_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def enter_search_query(self, query):
        """
        Enters a search query into the home page search bar.

        Uses WebDriverWait to wait up to 15 seconds until the search bar is clickable.

        :param query: The search query to enter.
        """
        home_page_search_bar = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_PAGE_SEARCH_BAR))
        )
        home_page_search_bar.clear()
        home_page_search_bar.send_keys(query)

    def click_search_button(self):
        """
        Clicks the search button on the home page search bar.

        Uses WebDriverWait to wait up to 15 seconds until the search button is clickable.
        """
        search_button_home_bar = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON_HOME_BAR))
        )
        search_button_home_bar.click()

    def is_hello_user_message_displayed(self):
        """
        Checks if the 'Hello User' message is displayed.

        Uses WebDriverWait to wait up to 15 seconds until the message element is visible.

        :return: True if the message is visible, False otherwise.
        """
        hello_user_message = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.HELLO_USER_MESSAGE))
        )
        return hello_user_message.is_displayed()

    def click_profile_button(self):
        """
        Clicks the profile button.

        Uses WebDriverWait to wait up to 15 seconds until the profile button is clickable.
        """
        profile_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_BUTTON))
        )
        profile_button.click()

    def click_profile_favorite_libraries_button(self):
        """
        Clicks the favorite libraries button in the profile menu.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        profile_favorite_libraries_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_FAVORITE_LIBRARIES_BUTTON))
        )
        profile_favorite_libraries_button.click()

    def click_profile_lists_button(self):
        """
        Clicks the lists button in the profile menu.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        profile_lists_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LISTS_BUTTON))
        )
        profile_lists_button.click()

    def click_profile_saved_searches_button(self):
        """
        Clicks the saved searches button in the profile menu.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        profile_saved_searches_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_SAVED_SEARCHES_BUTTON))
        )
        profile_saved_searches_button.click()

    def click_filter_button(self):
        """
        Clicks the advanced search filter button.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        filter_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.FILTER_BUTTON))
        )
        filter_button.click()

    def click_format_filter_dropdown_button(self):
        """
        Clicks the format filter dropdown button.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        format_filter_dropdown_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.FORMAT_FILTER_DROPBOX_BUTTON))
        )
        format_filter_dropdown_button.click()

    def click_music_cd_dropbox_option(self):
        """
        Clicks the music CD option in the format filter dropdown.

        Uses WebDriverWait to wait up to 15 seconds until the option is clickable.
        """
        music_cd_dropbox_option = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.MUSIC_CD_DROPBOX_OPTION))
        )
        music_cd_dropbox_option.click()

    def click_confirm_search_button(self):
        """
        Clicks the confirm search button in the advanced search.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        confirm_search_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_SEARCH_BUTTON))
        )
        confirm_search_button.click()

    def click_quit_dropbox_button(self):
        """
        Clicks the quit button to close the dropdown.

        Uses WebDriverWait to wait up to 15 seconds until the button is clickable.
        """
        quit_dropbox_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.QUIT_DROPBOX_BUTTON))
        )
        quit_dropbox_button.click()

    def search_book_flow(self, search_text):
        """
        Executes the flow to search for a book by entering the search text and clicking the search button.

        :param search_text: The search query to enter.
        """
        self.enter_search_query(search_text)
        self.click_search_button()
