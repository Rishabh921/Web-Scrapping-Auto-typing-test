from selenium import webdriver
import pyautogui
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
import date
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.ratatype.com/typing-test/test/")

start = driver.find_element_by_id("startButton")
#search.send_keys("test")
start.send_keys(Keys.RETURN)


content = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "mainTxt"))
)
print(content.text)
for char in content.text:
    pyautogui.typewrite(char)
    

# except:
#     driver.quit()
