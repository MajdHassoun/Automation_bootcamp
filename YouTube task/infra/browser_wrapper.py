from selenium import webdriver
from infra.config_provider import ConfigProvider
import undetected_chromedriver as uc
from selenium import common as c


class BrowserWrapper:
    def __init__(self):
        self._driver = None
        self._config = ConfigProvider().load_config_json()
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)

    def get_driver(self, url):
        try:
            if self._config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self._config["browser"] == "Firefox":
                self._driver = webdriver.Firefox()
            else:
                print("Driver does not exist")

            self._driver.get(url)
            return self._driver

        except c.WebDriverException as e:
            print("Could not find web driver:", e)