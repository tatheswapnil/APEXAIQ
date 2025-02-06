"""
to scrap oracle linux site
url = https://en.wikipedia.org/wiki/Oracle_Linux
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://en.wikipedia.org/wiki/Oracle_Linux")
time.sleep(1)

# Function to scrape a table
def scrape_table(xpath):
    table = driver.find_element(By.XPATH, xpath)
    rows = table.find_elements(By.XPATH, ".//tr")

    headers = [header.text for header in rows[0].find_elements(By.XPATH, ".//th")]
    data = []

    for row in rows[1:]:
        cells = row.find_elements(By.XPATH, ".//th | .//td")
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    return pd.DataFrame(data, columns=headers)

# Scrape the table
df_1 = scrape_table("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[3]")
df_2 = scrape_table("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[4]")

def shift_values(df):
    for i, row in df.iterrows():
        if row.iloc[0] == row.iloc[1]:  
            df.iloc[i, 1:-1] = row.iloc[2:].values  
            df.iloc[i, -1] = ''  
    return df


df_1_fixed = shift_values(df_1)


df_1_fixed.to_csv("E:/ApexaIQ/APEXA_PART2/Selenium/csv/oracle_linux.csv", index=False, header=True)
df_2.to_csv("E:/ApexaIQ/APEXA_PART2/Selenium/csv/oracle_linux.csv", index=False, header=True, mode='a')

driver.quit()

print("CSV saved")
