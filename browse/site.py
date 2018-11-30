from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep 

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("http://codechef.com/node")
print("Headless Firefox Initialized")
print("Done") 
input('Press anything to quit') 
print("Finished") 
driver.quit()