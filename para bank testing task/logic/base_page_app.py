from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    UPPER_LOGO = '//img[@alt = "ParaBank"]'
    HEADER_CAPTION = '//p[@class = "caption"]'
    SOLUTIONS_TITLE = '//li[@class = "Solutions"]'
    ABOUT_US_HEADER_MENU = '//ul[@class = "leftmenu"]//a[text() = "About Us"]'
    SERVICES_HEADER_MENU = '//ul[@class = "leftmenu"]//a[text() = "Services"]'
    PRODUCTS_HEADER_MENU = '//ul[@class = "leftmenu"]//a[text() = "Products"]'
    LOCATIONS_HEADER_MENU = '//ul[@class = "leftmenu"]//a[text() = "Locations"]'
    ADMIN_PAGE_HEADER_MENU = '//ul[@class = "leftmenu"]//a[text() = "Admin Page"]'
    RIGHT_SIDE_HOME_BUTTON = '//ul[@class="button"]//a[text()="home"]'
    RIGHT_SIDE_ABOUT_BUTTON = '//ul[@class="button"]//a[text()="about"]'
    RIGHT_SIDE_CONTACT_BUTTON = '//ul[@class="button"]//a[text()="contact"]'
    FOOTER_HOME_BUTTON = '//div[@id="footerPanel"]//a[text() = "Home"]'
    FOOTER_ABOUT_US_BUTTON = '//div[@id="footerPanel"]//a[text() = "About Us"]'
    FOOTER_SERVICES_BUTTON = '//div[@id="footerPanel"]//a[text() = "Services"]'
    FOOTER_PRODUCTS_BUTTON = '//div[@id="footerPanel"]//a[text() = "Products"]'
    FOOTER_LOCATIONS_BUTTON = '//div[@id="footerPanel"]//a[text() = "Locations"]'
    FOOTER_FORUM_BUTTON = '//div[@id="footerPanel"]//a[text() = "Forum"]'
    FOOTER_SITE_MAP_BUTTON = '//div[@id="footerPanel"]//a[text() = "Site Map"]'
    FOOTER_CONTACT_US_BUTTON = '//div[@id="footerPanel"]//a[text() = "Contact Us"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._upper_logo = self._driver.find_element(By.XPATH, self.UPPER_LOGO)
        self._header_caption = self._driver.find_element(By.XPATH, self.HEADER_CAPTION)
        self._solutions_title = self._driver.find_element(By.XPATH, self.SOLUTIONS_TITLE)
        self._about_us_header_menu = self._driver.find_element(By.XPATH, self.ABOUT_US_HEADER_MENU)
        self._services_header_menu = self._driver.find_element(By.XPATH, self.SERVICES_HEADER_MENU)
        self._products_header_menu = self._driver.find_element(By.XPATH, self.PRODUCTS_HEADER_MENU)
        self._locations_header_menu = self._driver.find_element(By.XPATH, self.LOCATIONS_HEADER_MENU)
        self._admin_page_header_menu = self._driver.find_element(By.XPATH, self.ADMIN_PAGE_HEADER_MENU)
        self._right_side_home_button = self._driver.find_element(By.XPATH, self.RIGHT_SIDE_HOME_BUTTON)
        self._right_side_about_button = self._driver.find_element(By.XPATH, self.RIGHT_SIDE_ABOUT_BUTTON)
        self._right_side_contact_button = self._driver.find_element(By.XPATH, self.RIGHT_SIDE_CONTACT_BUTTON)
        self._footer_home_button = self._driver.find_element(By.XPATH, self.FOOTER_HOME_BUTTON)
        self._footer_about_us_button = self._driver.find_element(By.XPATH, self.FOOTER_ABOUT_US_BUTTON)
        self._footer_services_button = self._driver.find_element(By.XPATH, self.FOOTER_SERVICES_BUTTON)
        self._footer_products_button = self._driver.find_element(By.XPATH, self.FOOTER_PRODUCTS_BUTTON)
        self._footer_locations_button = self._driver.find_element(By.XPATH, self.FOOTER_LOCATIONS_BUTTON)
        self._footer_forum_button = self._driver.find_element(By.XPATH, self.FOOTER_FORUM_BUTTON)
        self._footer_site_map_button = self._driver.find_element(By.XPATH, self.FOOTER_SITE_MAP_BUTTON)
        self._footer_contact_us_button = self._driver.find_element(By.XPATH, self.FOOTER_CONTACT_US_BUTTON)

    def click_upper_logo(self):
        self._upper_logo.click()

    def get_header_caption(self):
        return self._header_caption.text

    def click_solutions_title(self):
        self._solutions_title.click()

    def click_about_us_header_menu(self):
        self._about_us_header_menu.click()

    def click_services_header_menu(self):
        self._services_header_menu.click()

    def click_products_header_menu(self):
        self._products_header_menu.click()

    def click_locations_header_menu(self):
        self._locations_header_menu.click()

    def click_admin_page_header_menu(self):
        self._admin_page_header_menu.click()

    def click_right_side_home_button(self):
        self._right_side_home_button.click()

    def click_right_side_about_button(self):
        self._right_side_about_button.click()

    def click_right_side_contact_button(self):
        self._right_side_contact_button.click()

    def click_footer_home_button(self):
        self._footer_home_button.click()

    def click_footer_about_us_button(self):
        self._footer_about_us_button.click()

    def click_footer_services_button(self):
        self._footer_services_button.click()

    def click_footer_products_button(self):
        self._footer_products_button.click()

    def click_footer_locations_button(self):
        self._footer_locations_button.click()

    def click_footer_forum_button(self):
        self._footer_forum_button.click()

    def click_footer_site_map_button(self):
        self._footer_site_map_button.click()

    def click_footer_contact_us_button(self):
        self._footer_contact_us_button.click()
