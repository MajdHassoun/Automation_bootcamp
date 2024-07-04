import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class TestDragAndDropExample(unittest.TestCase):
    def test_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://www.solnet.co.il/klondike3")
        source_element = driver.find_element(By.XPATH, '//div[@id = "card47"]')
        target_element = driver.find_element(By.XPATH, '//div[@id = "card35"]')
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()
        time.sleep(2)
        driver.quit()
