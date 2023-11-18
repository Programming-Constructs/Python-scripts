# import modules 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome() 
  
# url 
driver.get('https://esolangs.org/wiki/Language_list') 
  

# find web links 
link = driver.find_elements(By.TAG_NAME, 'a') 
  
# using len function count how many links 
print(len(link)) 