import json

class _users_(object):

    def __init__(self,mode):
        self.mode = mode
        self.users = None
        self.userFile = None

    def openFile(self):
        self.userFile = open("users.json",self.mode)
        self.users = json.load(self.userFile)

    """def addUser(self):
        uname = input()
        email = input()
        new = {"username": uname,"email": email}
        json.dump(new, self.userFile)"""
    
    def showUsers(self):
        for user in self.users:
            for param in user:
                print("%s : %s" % (param,user[param]))
    
    def userDetail(self,param):
        return self.users[0][param]

    def closeFile(self):
        self.userFile.close()
        if self.userFile.closed :
            del self.userFile

"""
(decomment this block for testing only)
if __name__ == "__main__" :
    pass
"""