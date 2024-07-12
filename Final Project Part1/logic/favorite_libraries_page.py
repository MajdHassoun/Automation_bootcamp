from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class FavoriteLibrariesPage(BasePageApp):
    """
    FavoriteLibrariesPage class extends BasePageApp and provides methods for interacting with
    elements related to favorite libraries.
    """

    # XPaths for elements on the favorite libraries page
    FAVORITE_LIBRARY_NAME = '//div[@class="MuiBox-root mui-69i1ev"]//p[@class = "MuiTypography-root MuiTypography-body1 mui-1qm8jy7"]'
    REMOVE_FAVORITE_BUTTON = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge mui-hrq81h"]'
    CONFIRM_REMOVE_BUTTON = '//button[@data-testid="remove-favorite-library-dialog-button"]'
    NO_LIBRARIES_MESSAGE = '//h3[text()="You do not have any favorite libraries"]'

    def __init__(self, driver):
        """
        Initializes the FavoriteLibrariesPage instance.

        :param driver: WebDriver instance used for interacting with the browser.
        """
        super().__init__(driver)

    def get_favorite_library_name(self):
        """
        Retrieves the name of the favorite library.

        Uses WebDriverWait to wait up to 10 seconds until the favorite library name element is visible.

        :return: The text of the favorite library name element.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.FAVORITE_LIBRARY_NAME))
        )
        return element.text

    def click_remove_favorite_button(self):
        """
        Clicks the remove favorite button.

        Uses WebDriverWait to wait up to 10 seconds until the remove favorite button is clickable.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.REMOVE_FAVORITE_BUTTON))
        )
        element.click()

    def click_confirm_remove_button(self):
        """
        Clicks the confirm remove button.

        Uses WebDriverWait to wait up to 10 seconds until the confirm remove button is present.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CONFIRM_REMOVE_BUTTON))
        )
        element.click()

    def get_no_libraries_message(self):
        """
        Checks if the 'No favorite libraries' message is displayed.

        Uses WebDriverWait to wait up to 10 seconds until the message element is visible.

        :return: True if the message is visible, False otherwise.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NO_LIBRARIES_MESSAGE))
        )
        return element.is_displayed()

    def remove_favorite_library_flow(self):
        """
        Executes the flow to remove a favorite library by clicking the remove favorite button
        and confirm remove button.
        """
        self.click_remove_favorite_button()
        self.click_confirm_remove_button()
