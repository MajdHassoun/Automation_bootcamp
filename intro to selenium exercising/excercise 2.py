import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ultimateqa.com/complicated-page")

for i in range(0, 12):
    driver.find_element(By.XPATH, f"//a[@class='et_pb_button et_pb_button_{i} et_pb_bg_layout_light']").click()
    time.sleep(0.4)

driver.find_element(By.XPATH,
                    '//li[contains(@class,"et_pb_social_media_follow_network_0")]//a[@title="Follow on Twitter"]') \
    .click()
time.sleep(2)

while driver.current_url != "https://ultimateqa.com/complicated-page":
    driver.back()

driver.find_element(By.XPATH,
                    '//li[contains(@class,"et_pb_social_media_follow_network_3")]//a[@title="Follow on Facebook"]').click()
time.sleep(2)
while driver.current_url != "https://ultimateqa.com/complicated-page":
    driver.back()
time.sleep(3)

driver.find_element(By.XPATH, '//input[@id= "et_pb_contact_name_0"]').send_keys("Majd Hassoun")
driver.find_element(By.XPATH, '//input[@id="et_pb_contact_email_0"]').send_keys("majd@gmail.com")
driver.find_element(By.XPATH, '//textarea[@id="et_pb_contact_message_0"]').send_keys("solve this task")

# a = driver.find_element(By.XPATH, '//input[@class="input et_pb_contact_captcha" and @data-first_digit="15"]').text
# b = a.split()
# print(b)
# time.sleep(2)
