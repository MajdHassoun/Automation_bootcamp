from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class HomePage(BasePage):
    SIGN_IN_BUTTON = '//a[text() = "Sign in"]'
    COOKIES_BUTTON = '(//button[text() = "Accept all cookies"])[1]'
    HOME_PAGE_SEARCH_BAR = '//input[@id ="home-page-search-box"]'
    SEARCH_BUTTON_HOME_BAR = '//button[@data-testid ="search-button"]'
    HOME_SEARCH_BAR_DROP_BOX = '//main//div[@aria-haspopup ="listbox"]'
    HOME_DROP_BOX_ITEMS_OPTION = '//li[@data-testid ="hero-search-box-option-items"]"]'
    HOME_DROP_BOX_LIBRARIES_OPTION = '//li[@data-testid ="hero-search-box-option-lib"]'
    HOME_DROP_BOX_LISTS_OPTION = '//li[@data-testid ="hero-search-box-option-lists"]'
    HELLO_USER_MESSAGE = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_BUTTON = '//header//p[@class="MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    PROFILE_FAVORITE_LIBRARIES_BUTTON = '//li[@data-value = "favorite-libraries"]'
    PROFILE_LISTS_BUTTON = '//li[@data-value = "my-lists"]'
    PROFILE_SAVED_SEARCHES_BUTTON = '//li[@data-value = "saved-searches"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        self._cookies_button = self._driver.find_element(By.XPATH, self.COOKIES_BUTTON)
        self._home_page_search_bar = self._driver.find_element(By.XPATH, self.HOME_PAGE_SEARCH_BAR)
        self._search_button_home_bar = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON_HOME_BAR)
        self._home_search_bar_drop_box = self._driver.find_element(By.XPATH, self.HOME_SEARCH_BAR_DROP_BOX)

    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    def click_on_cookies(self):
        self._cookies_button.click()

    def enter_search_text(self, text):
        self._home_page_search_bar.clear()
        self._home_page_search_bar.send_keys(text)

    def click_search_button(self):
        self._search_button_home_bar.click()

    def click_drop_box_items_option(self):
        drop_box_items_option = self._driver.find_element(By.XPATH, self.HOME_DROP_BOX_ITEMS_OPTION)
        drop_box_items_option.click()

    def click_drop_box_libraries_option(self):
        drop_box_libraries_option = self._driver.find_element(By.XPATH, self.HOME_DROP_BOX_LIBRARIES_OPTION)
        drop_box_libraries_option.click()

    def click_drop_box_lists_option(self):
        drop_box_lists_option = self._driver.find_element(By.XPATH, self.HOME_DROP_BOX_LISTS_OPTION)
        drop_box_lists_option.click()

    def is_hello_user_message_visible(self):
        hello_user_message = self._driver.find_element(By.XPATH, self.HELLO_USER_MESSAGE)
        return hello_user_message.is_displayed()

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
