from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
import time
import sys
from config import chromePath



options = webdriver.ChromeOptions()
options.add_argument(chromePath)
#options.headless = True


s='./chromedriver'
driver = webdriver.Chrome(s,options=options)
driver.get("https://web.whatsapp.com/")
#driver.implicitly_wait(5)
#time.sleep(10)


contact = 'Meal'
search_box = WebDriverWait(driver,500).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]'))
)


contact = 'Meal'
searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchBox.send_keys(contact)
searchBox.send_keys(Keys.ENTER)

driver.implicitly_wait(5)
msg = '@Frank\nAutomating\n..Testing_Meal_Bot..\n'
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
msg_box.send_keys(msg)
msg_box.send_keys(Keys.ENTER)



print('DONE')






