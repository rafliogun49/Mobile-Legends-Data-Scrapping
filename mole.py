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
time.sleep(10)
html = driver.page_source
with open("all_ranks.html", "w", encoding="utf-8") as file:
    file.write(html)

rank_buttons = driver.find_element(By.CLASS_NAME, "switch").find_elements(By.XPATH, ".//*")
rank_buttons[1].click()
time.sleep(10)
html = driver.page_source
with open("mythic.html", "w", encoding="utf-8") as file:
    file.write(html)

rank_buttons[2].click()
time.sleep(10)
html = driver.page_source
with open("mythical_glory.html", "w", encoding="utf-8") as file:
    file.write(html)

driver.quit()