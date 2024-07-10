from selenium.webdriver.common.by import By

from logic.base_page_app import BasePageApp


class FavoriteLibrariesPage(BasePageApp):
    FAVORITE_LIBRARY_NAME = '//div[@class="MuiBox-root mui-69i1ev"]//p[@class = "MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    REMOVE_FAVORITE_BUTTON = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge mui-hrq81h"]'
    CONFIRM_REMOVE_BUTTON = 'data-testid="remove-favorite-library-dialog-button"'
    NO_LIBRARIES_MESSAGE = '//h3[text()="You do not have any favorite libraries"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._favorite_library_name = self._driver.find_element(By.XPATH, self.FAVORITE_LIBRARY_NAME)
        self._remove_favorite_button = self._driver.find_element(By.XPATH, self.REMOVE_FAVORITE_BUTTON)

    def get_favorite_library_name(self):
        return self._favorite_library_name.text

    def click_remove_favorite_button(self):
        self._remove_favorite_button.click()

    def click_confirm_remove_button(self):
        confirm_remove_button = self._driver.find_element(By.XPATH, self.CONFIRM_REMOVE_BUTTON)
        confirm_remove_button.click()

    def get_no_libraries_message(self):
        no_libraries_message = self._driver.find_element(By.XPATH, self.NO_LIBRARIES_MESSAGE)
        return no_libraries_message.is_displayed()
