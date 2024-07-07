import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utiles import Utiles
from logic.home_page import HomePage
from logic.register_page import RegisterPage
from logic.successful_register_page import SuccessfulRegisterPage
from logic.utiles_logic import UtilesLogic


class ValidRegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def test_valid_register(self):
        self.home_page.click_register_button()
        register_page_obj = RegisterPage(self.driver)
        register_page_obj.fill_first_name_input(Utiles.generate_random_string(4))
        register_page_obj.fill_last_name_input(Utiles.generate_random_string(4))
        register_page_obj.fill_address_input(UtilesLogic.get_random_israel_detail("ADDRESSES"))
        register_page_obj.fill_city_input(UtilesLogic.get_random_israel_detail("CITIES"))
        register_page_obj.fill_state_input(UtilesLogic.get_random_israel_detail("STATES"))
        register_page_obj.fill_zip_code_input(UtilesLogic.get_random_israel_detail("ZIP_CODES"))
        register_page_obj.fill_phone_input(Utiles.generate_random_phone_number(10))
        register_page_obj.fill_ssn_input(UtilesLogic.get_random_israel_detail("SSNS"))
        register_page_obj.fill_username_input(Utiles.generate_random_string(5))
        random_generated_password = Utiles.generate_random_string(5)
        register_page_obj.fill_password_input(random_generated_password)
        register_page_obj.fill_confirm_input(random_generated_password)
        register_page_obj.click_on_register_button()
        time.sleep(2)
        successful_register_obj = SuccessfulRegisterPage(self.driver)
        self.assertTrue(successful_register_obj.welcome_message_displayed())
        self.assertTrue(successful_register_obj.confirmation_message_displayed())
