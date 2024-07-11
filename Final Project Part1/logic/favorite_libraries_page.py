from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class FavoriteLibrariesPage(BasePageApp):
    FAVORITE_LIBRARY_NAME = '//div[@class="MuiBox-root mui-69i1ev"]//p[@class = "MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    REMOVE_FAVORITE_BUTTON = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge mui-hrq81h"]'
    CONFIRM_REMOVE_BUTTON = 'data-testid="remove-favorite-library-dialog-button"'
    NO_LIBRARIES_MESSAGE = '//h3[text()="You do not have any favorite libraries"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_favorite_library_name(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.FAVORITE_LIBRARY_NAME)))

        return element.text

    def click_remove_favorite_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE_FAVORITE_BUTTON)))

        element.click()

    def click_confirm_remove_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_REMOVE_BUTTON)))

        element.click()

    def get_no_libraries_message(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_LIBRARIES_MESSAGE)))

        return element.is_displayed()
