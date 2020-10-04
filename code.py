from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 

intervalPress=0.25
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.ratatype.com/typing-test/test/")

start = driver.find_element_by_id("startButton")
#search.send_keys("test")
start.send_keys(Keys.RETURN)


content = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "mainTxt"))
)
print(content.text)
for word in content.text:
    pyautogui.write(word, interval=intervalPress)
driver.quit()

# except:
#     driver.quit()
