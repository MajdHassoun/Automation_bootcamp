import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Go to login page')]")

login_button.send_keys(Keys.RETURN)
driver.implicitly_wait(2)

email_input = driver.find_element(By.ID, "user[email]")
password_input = driver.find_element(By.ID, "user[password]")
email_input.send_keys("majd12hassoun@gmail.com")
password_input.send_keys("11111111")
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()
print(driver.find_element(By.XPATH, '//li[@class="form-error__list-item"]').text)
time.sleep(5)
driver.back()
driver.back()

button_button = driver.find_element(By.XPATH, "//a[contains(text(),'Click Me')]")
button_button.send_keys(Keys.RETURN)
second_button_to_click_res = driver.find_element(By.XPATH, "//h1[contains(text(),'Button success')]")
print(second_button_to_click_res.text)
time.sleep(5)
driver.back()

click_button_using_className = driver.find_element(By.CLASS_NAME, 'buttonClass')
click_button_using_className.send_keys(Keys.RETURN)
time.sleep(5)
driver.back()


driver.quit()
