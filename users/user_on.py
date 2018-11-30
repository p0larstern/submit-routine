import pickle,getpass

class user(object):

    def __init__(self):
        self.username = None
        self.password = None

    def getStuff(self):
        return (self.username,self.password)

    def putStuff(self):
        self.username = input("username? ")
        self.password = getpass.getpass(prompt="password? ")

class userUtil(object):

    def __init__(self,userObj):
        self.userObj = userObj
        self.fileName = "user_on.dat"
        self.fileObj = None

    def saveUser(self):
        pickle.dump(self.userObj,self.fileObj)
        self.closeFile()
        print("User credentials saved.")

    def loadUser(self):
        if self.fileObj == None :
            print("No data file available!")
            return None
        return pickle.load(self.fileObj)

    def openFile(self,mode):
        self.fileObj = open(self.fileName,mode)

    def closeFile(self):
        self.fileObj.close()
        self.fileObj = None