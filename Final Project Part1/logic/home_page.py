from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class HomePage(BasePage):
    SIGN_IN_BUTTON = '//a[text() = "Sign in"]'
    COOKIES_BUTTON = '(//button[text() = "Accept all cookies"])[1]'
    HOME_PAGE_SEARCH_BAR = '//input[@id ="home-page-search-box"]'
    SEARCH_BUTTON_HOME_BAR = '//button[@data-testid ="search-button"]'
    HOME_SEARCH_BAR_DROP_BOX = '//main//div[@aria-haspopup ="listbox"]'  #
    HOME_DROP_BOX_ITEMS_OPTION = '//li[@data-testid ="hero-search-box-option-items"]"]'  #
    HOME_DROP_BOX_LIBRARIES_OPTION = '//li[@data-testid ="hero-search-box-option-lib"]'  #
    HOME_DROP_BOX_LISTS_OPTION = '//li[@data-testid ="hero-search-box-option-lists"]'  #
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
        super().__init__(driver)

    def click_sign_in(self):
        sign_in_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGN_IN_BUTTON))
        )
        sign_in_button.click()

    def click_accept_cookies(self):
        cookies_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def enter_search_query(self, query):
        home_page_search_bar = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_PAGE_SEARCH_BAR))
        )
        home_page_search_bar.clear()
        home_page_search_bar.send_keys(query)

    def click_search_button(self):
        search_button_home_bar = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON_HOME_BAR))
        )
        search_button_home_bar.click()

    def click_home_search_bar_drop_box(self):
        home_search_bar_drop_box = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_SEARCH_BAR_DROP_BOX))
        )
        home_search_bar_drop_box.click()

    def click_home_drop_box_items_option(self):
        home_drop_box_items_option = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_DROP_BOX_ITEMS_OPTION))
        )
        home_drop_box_items_option.click()

    def click_home_drop_box_libraries_option(self):
        home_drop_box_libraries_option = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_DROP_BOX_LIBRARIES_OPTION))
        )
        home_drop_box_libraries_option.click()

    def click_home_drop_box_lists_option(self):
        home_drop_box_lists_option = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.HOME_DROP_BOX_LISTS_OPTION))
        )
        home_drop_box_lists_option.click()

    def is_hello_user_message_displayed(self):
        hello_user_message = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.HELLO_USER_MESSAGE))
        )
        return hello_user_message.is_displayed()

    def click_profile_button(self):
        profile_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_BUTTON))
        )
        profile_button.click()

    def click_profile_favorite_libraries_button(self):
        profile_favorite_libraries_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_FAVORITE_LIBRARIES_BUTTON))
        )
        profile_favorite_libraries_button.click()

    def click_profile_lists_button(self):
        profile_lists_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_LISTS_BUTTON))
        )
        profile_lists_button.click()

    def click_profile_saved_searches_button(self):
        profile_saved_searches_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.PROFILE_SAVED_SEARCHES_BUTTON))
        )
        profile_saved_searches_button.click()

    def click_filter_button(self):
        filter_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.FILTER_BUTTON))
        )
        filter_button.click()

    def click_format_filter_dropdown_button(self):
        format_filter_dropdown_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.FORMAT_FILTER_DROPBOX_BUTTON))
        )
        format_filter_dropdown_button.click()

    def click_music_cd_dropbox_option(self):
        music_cd_dropbox_option = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.MUSIC_CD_DROPBOX_OPTION))
        )
        music_cd_dropbox_option.click()

    def click_confirm_search_button(self):
        confirm_search_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_SEARCH_BUTTON))
        )
        confirm_search_button.click()

    def click_quit_dropbox_button(self):
        quit_dropbox_button = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.QUIT_DROPBOX_BUTTON))
        )
        quit_dropbox_button.click()

    def search_book_flow(self, search_text):
        self.enter_search_query(search_text)
        self.click_search_button()
