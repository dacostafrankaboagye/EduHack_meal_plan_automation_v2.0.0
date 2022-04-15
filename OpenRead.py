
from selenium import webdriver
from selenium.webdriver.common.by import By

def Id_info():  
    # get the ID from the database
    '''
    using txt file as a test
    '''
    with open('ListOfID.txt', 'r') as IDList:
        for i in IDList:
            id = i.strip()

     

Id_info()



def perform_operation(driver):
    with open('db.txt','a') as dbT:
        for i in range(1,10): # will they have more than 10 items???
            ab = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/table/tbody/tr['+str(i)+']')
            dbT.write('==')
            for j in ab:                 
                #dbT.write((j.get_attribute('innerText')).replace('    ','') ) 
                dbT.write(str((j.get_attribute('innerText'))))  






