import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_remove_page import AddRemoveElementsPage
from logic.challenging_dom_page import ChallengingDomPage
from logic.checkboxes_page import CheckboxesPage
from logic.context_menu_page import ContextMenuPage
from logic.disappearing_elements_page import DisappearingElementsPage
from logic.drag_and_drop_page import DragAndDropPage
from logic.dropdown_list_page import DropDownListPage
from logic.dynamic_content_page import DynamicContentPage
from logic.dynamic_controls_page import DynamicControlsPage
from logic.home_page import HomePage


class Test(unittest.TestCase):
    browser = BrowserWrapper()
    config = browser.config

    def test_add_remove_element(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_add_remove_link()

        time.sleep(0.5)
        add_remove_elements = AddRemoveElementsPage(driver)
        add_remove_elements.click_on_add_elements_counts(5)
        time.sleep(0.5)

        add_remove_elements.click_on_delete(3)
        time.sleep(1)

    def test_challenging_dom(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_challenging_dom_link()
        time.sleep(0.5)
        dom_challenge = ChallengingDomPage(driver)
        dom_challenge.click_on_edit(5)
        time.sleep(2)
        dom_challenge.click_on_delete(3)
        time.sleep(0.5)

    def test_checkbox_click(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_checkboxes_link()
        time.sleep(0.5)
        checkbox_page = CheckboxesPage(driver)
        checkbox_page.click_on_checkbox()
        checkbox_page.unclick_checkbox()
        time.sleep(1)

    def test_context_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_context_menu_link()
        time.sleep(0.5)
        context_menu_obj = ContextMenuPage(driver)
        context_menu_obj.click_on_the_box()
        time.sleep(0.5)

    def test_disappearing_elements(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_disappearing_elements_link()
        time.sleep(0.5)
        disappearing_elements_obj = DisappearingElementsPage(driver)
        disappearing_elements_obj.click_home_button()
        time.sleep(1)
        driver.back()
        disappearing_elements_obj.click_about_button()
        time.sleep(1)
        driver.back()
        disappearing_elements_obj.click_contact_us_button()
        time.sleep(1)
        driver.back()
        disappearing_elements_obj.click_portfolio_button()
        time.sleep(1)
        driver.back()

    def test_drag_and_drop(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_drag_and_drop_link()
        time.sleep(0.5)
        drag_and_drop_obj = DragAndDropPage(driver)
        drag_and_drop_obj.drag_and_drop_l_to_r()
        time.sleep(0.3)
        drag_and_drop_obj.drag_and_drop_r_to_l()

    def test_dropdown_window(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_dropdown_link()
        time.sleep(0.5)
        dropdown_obj = DropDownListPage(driver)
        dropdown_obj.pick_both_options_flow()

    def test_dynamic_content(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_dynamic_content_link()
        time.sleep(0.5)
        dynamic_content_obj = DynamicContentPage(driver)
        print(dynamic_content_obj.get_dynamic_content_text())
        print(dynamic_content_obj.get_image_src())
        time.sleep(0.5)
        dynamic_content_obj.refresh_page()
        time.sleep(0.5)
        print(dynamic_content_obj.get_dynamic_content_text())
        print(dynamic_content_obj.get_image_src())

    def test_dynamic_controls_checkbox(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_dynamic_controls_link()

        time.sleep(0.5)
        dcp = DynamicControlsPage(driver)

        time.sleep(1)
        dcp.click_on_checkbox()
        time.sleep(1)
        dcp.click_on_remove_button()
        time.sleep(1)
        dcp.click_on_checkbox_forced()
        time.sleep(5)
        driver.quit()

    def test_dynamic_controls_input(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(0.1)
        home_page = HomePage(driver)
        home_page.click_on_dynamic_controls_link()

        time.sleep(0.5)
        dcp = DynamicControlsPage(driver)

        time.sleep(1)
        dcp.click_on_enable_button()
        time.sleep(1)
        dcp.type_in_input("HELLO")
        time.sleep(1)
        dcp.click_on_disable_button()
        time.sleep(1)
        dcp.type_in_input_forced("BEY")
        time.sleep(5)
        driver.quit()
