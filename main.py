from selenium import webdriver
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

search_term = 'giraffe'

currentpath = os.getcwd()
if ' ' in search_term:
    downloaddir = search_term.replace(' ','_')
else:
    downloaddir = search_term
downloadpath = currentpath + '/' + downloaddir
if not os.path.exists(downloadpath):
    os.mkdir(downloadpath)


driver = webdriver.Chrome(currentpath + "/chromedriver")
driver.maximize_window()
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')
box = driver.find_element(by=By.XPATH,value='//*[@id="sbtc"]/div/div[2]/input')
box.send_keys(search_term)
box.send_keys(Keys.ENTER)

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="islmp"]/div/div/div/div/div[5]/input' )
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1,100):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(downloadpath+'/image ('+str(i)+').png')
    except:
        pass

driver.close()