from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# website that fixed my problem with selenium "https://www.scrapingbee.com/webscraping-questions/selenium/chromedriver-executable-needs-to-be-in-path/"
# https://sites.google.com/chromium.org/driver/
# https://selenium-python.readthedocs.io/

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://feedni.ink/discover/%D8%B9%D8%A7%D9%85")


link = driver.find_element(By.PARTIAL_LINK_TEXT, "kalkoaa.blogspot.com")
link.click()


time.sleep(20)

driver.quit()
