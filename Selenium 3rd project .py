import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# https://www.geeksforgeeks.org/selenium-python-tutorial/
# https://www.geeksforgeeks.org/locating-single-elements-in-selenium-python/
# https://selenium-python.readthedocs.io/locating-elements.html



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://authn.edx.org/login")
driver.implicitly_wait(10)


try:
    cooky_1 = driver.find_element(By.ID, "onetrust-reject-all-handler")
    cooky_1.click()
except: 
    print("No cookies is needed")

email = driver.find_element(By.ID,"emailOrUsername")
password = driver.find_element(By.ID,"password")


email.send_keys("your@email")
password.send_keys("your_password")
sing_in = driver.find_element(By.ID, "sign-in")
sing_in.click()

time.sleep(10)