from datetime import datetime, timedelta
from dateutil import parser
import bcrypt
import os
from sanitizeInput import sanitize


maxAttempts = 1

def getSE():
    return timedelta(minutes=2)

def getLLDelta():
    return timedelta(minutes=1)


def writeID(n):
    stized = sanitize(n)
    hn = bcrypt.hashpw(n.encode(),bcrypt.gensalt())
    with open("session.txt","wb") as d:
        d.write()
        d.close()
        
def writeLoginTime(n):
    with open("sessionTime.txt","w") as d:
        d.write(n)
        d.close()


def checkSession(p):
    with open("session.txt","rb") as d:
        osop = d.read()
        d.close()
        if(bcrypt.checkpw(p.encode(), osop)):
            return True
    return False

#validate username
def checkLoginTime():
    with open("sessionTime.txt", "r") as d:
        timestring = d.read()
        loginTime = parser.parse(timestring)
        timeSince = datetime.now() - loginTime
        d.close()
        if(timeSince<getSE()):
            return True
    return False
    
def resetAttemptCount(userID):
    with open(userID+".txt","w") as d:
            d.write("0")
            d.close()
    

def getLoginAttempts(userID):
    if(os.path.exists(userID+".txt")):
        with open(userID+".txt","r") as d:
            attempts = d.read()
            d.close()
            print(int(attempts))
            return int(attempts)
    resetAttemptCount(userID)
    return 0


def addLoginAttempt(userID):
    aCount = getLoginAttempts(userID)
    aCount += 1
    with open(userID+".txt","w") as d:
            d.write(str(aCount))
            d.close()

def checkAttemptCount(userID):
    lastLogTime = getLastLogTime(userID)
    llDelta = datetime.now() - lastLogTime
    if(llDelta>getLLDelta()):
        resetAttemptCount(userID)
    if (getLoginAttempts(userID)>maxAttempts):
        return False
    return True

def WriteLogTime(userID):
    with open(userID+"ll.txt","w") as d:
        d.write(str(datetime.now()))
        d.close()

def getLastLogTime(userID):
    if(os.path.exists(userID+"ll.txt")==False):
        WriteLogTime(userID)
        return datetime.now()
    else:  
        with open(userID+"ll.txt","r") as d:
            time = parser.parse(d.read())
            d.close()
            return time
