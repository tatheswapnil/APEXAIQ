"""Kb Corel Scrapper"""

#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
# from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()

#chrome instance
driver.get("https://kb.corel.com/en/125936")
time.sleep(1)
 
tables = driver.find_element(By.XPATH, ".//table")
all_table_rows = tables.find_elements(By.XPATH, ".//tr")
 
list_of_rows = []
 
for each_row in all_table_rows:
    list_of_data = []
    all_data = each_row.find_elements(By.XPATH, ".//td")
    for data in all_data:
        list_of_data.append(data.text)
        
    list_of_rows.append(list_of_data)

 
 
df = pd.DataFrame(list_of_rows[1:], columns = list_of_rows[0])
df.to_csv("E:\ApexaIQ\APEXA_PART2\Selenium\csv/korel.csv", index=False)
print("CSV saved")

