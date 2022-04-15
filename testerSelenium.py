
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from OpenRead import *
#import re
#os.environ['PATH'] += r"C:/WebDrivers"

options = webdriver.ChromeOptions()
options.headless = True



driver = webdriver.Chrome('./chromedriver',chrome_options=options)
driver.get("http://mplan.ashesi.edu.gh/subscriber/#!/")
driver.implicitly_wait(5)

un = '70722023' # the id



un_tb = driver.find_element_by_class_name('search-by-id')
un_tb.send_keys(un)

login = driver.find_element_by_class_name("search-by-id-btn")
login.submit()
#driver.close()

driver.implicitly_wait(5)

a = []

try:
    # with open('db.txt','a') as dbT:
    #     for i in range(1,5):
    #         ab = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/table/tbody/tr['+str(i)+']')
    #         dbT.write('==')
    #         for j in ab:
                 
    #             #dbT.write((j.get_attribute('innerText')).replace('    ','') ) 
    #             dbT.write(str((j.get_attribute('innerText'))))  
    
    perform_operation(driver=driver)
                                
except:
    print('Nil')

# # to traverse throu
driver.close ()



def update(): pass


