from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# infra
driver = webdriver.Chrome()
# infra        #logic
driver.get("https://www.youtube.com/?app=desktop")
# logic
search_input = driver.find_element(By.NAME, "search_query")
search_input.send_keys("Vini JR")
search_input.send_keys(Keys.RETURN)
# infra
driver.quit()
