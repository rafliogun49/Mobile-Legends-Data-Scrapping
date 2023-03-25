from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


driver = webdriver.Chrome("chromedriver.exe")
url = "https://www.mobilelegends.com/id/rank"
driver.get(url)
print("sleep pertama")
time.sleep(5)
rank_buttons = driver.find_element(By.CLASS_NAME, "switch").find_elements(By.XPATH, ".//*")
print(rank_buttons)
print("sleep kedua")
time.sleep(5)
# html = driver.page_source
# with open("mythic.html", "w", encoding="utf-8") as file:
#     file.write(html)
# ranks = driver.find_elements(By.CLASS_NAME, "rank-item")
# last_ranks = ranks[-1]
# print(last_ranks)
# ActionChains(driver)\
#     .scroll_to_element(last_ranks)\
#     .perform()

# time.sleep(2)
# ranks = driver.find_elements(By.CLASS_NAME, "rank-item")
# last_ranks = ranks[-1]
# print(last_ranks)
# ActionChains(driver)\
#     .scroll_to_element(last_ranks)\
#     .perform()
# ranks = driver.find_elements(By.CLASS_NAME, "rank-item")
# # last_ranks = ranks[-1]
# last_ranks = ranks[-1].rect['y']
# ActionChains(driver)\
#     .scroll_by_amount(0, 1000)\
#     .perform()


# for hero in ranks:
#     name = hero.find_element(By.CLASS_NAME,'name').text
#     print(name)
# time.sleep(2)

driver.quit()