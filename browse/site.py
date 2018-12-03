from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC

class site(object):

    def __init__(self,head):
        self.url = "http://codechef.com"
        self.options = Options()
        self.options.headless = head
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
        
    def quit(self):
        self.driver.quit()

    def submit(self, qcode, srcPath, lang):
        self.driver.get(self.url+"/submit/"+qcode.upper())
        self.fileEle = self.driver.find_element_by_id("edit-sourcefile")
        self.fileEle.send_keys(srcPath)
       
        self.langEle = self.driver.find_element_by_name("language")
        for option in self.langEle.find_elements_by_tag_name('option'):
            if option.value == lang :
                option.click()
                break
        
        self.submitBtn = self.driver.find_element_by_name("op")
        self.submitBtn.click()

    def logout(self):
        self.driver.get(self.url+"/logout")