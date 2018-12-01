from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

class site(object):

    def __init__(self):
        self.url = "http://codechef.com"
        self.options = Options()
        self.options.headless = True
        self.driver = None

    def start(self):
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get(self.url)
    
    def login(self, uname, passw):
        self.unameEle = self.driver.find_element_by_name("name")
        self.unameEle.send_keys(uname)
        self.passwEle = self.driver.find_element_by_name("pass")
        self.passwEle.send_keys(passw)
        self.loginBtn = self.driver.find_element_by_name("op")
        self.loginBtn.click()
        
    def getQ(self, qcode):
        self.driver.get(self.url+"/problems/"+qcode.upper())

    def quit(self):
        self.driver.quit()
"""
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
driver.get("http://codechef.com/node")
print("Headless Firefox Initialized")
print("Done") 
input('Press anything to quit') 
print("Finished") 
driver.quit()
"""