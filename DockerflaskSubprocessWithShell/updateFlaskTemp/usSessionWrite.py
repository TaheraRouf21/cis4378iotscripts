import subprocess
import bcrypt
from sanitizeInput import sanitize, unsanitize

def writeSessionID(n):
    pwHash = bcrypt.hashpw(n.encode(),bcrypt.gensalt())
    print("write session: " +n)
    print("write session: "+pwHash.decode())
    cmmd = "/bin/bash -c \""
    cmmd += "echo '" + sanitize(pwHash.decode())
    cmmd+="'| tee session.txt\"" 
    result = subprocess.run([cmmd], shell=True,capture_output=True)

def writeLoginTime(n):
    #unameHash = bcrypt.hashpw(tpw.encode(),bcrypt.gensalt())
    cmmd = "/bin/bash -c \""
    cmmd += "echo " + n
    cmmd+=" | tee sessionTime.txt\"" 
    result = subprocess.run([cmmd], shell=True)

def checkSession(p):
    print(p)
    result = subprocess.run(["/bin/rbash -c \"cat /home/app/session.txt\""],shell=True,capture_output=True)
    hsalt = result.stdout.decode('utf-8')
    hsalt = hsalt.strip()
    if(bcrypt.checkpw(p.encode(),hsalt.encode())):
        return True
    return False

def getLT():
    #hn = u.encode()
    result = subprocess.run(["/bin/rbash -c \"cat /home/app/sessionTime.txt\""],shell=True,capture_output=True)
    osop = result.stdout.decode()
    osop = osop.strip()
    print("read time: "+ osop)
    return osop

    #deep purple