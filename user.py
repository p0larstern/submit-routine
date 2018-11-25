import json
users = None

def openFile(mode):
    with open("users.json", mode) as userFile:
        global users
        users = json.load(userFile)

if __name__ == "__main__":
    openFile("r")
    for user in users:
        for param in user:
            print("%s : %s" % (param,user[param]))