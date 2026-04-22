import bcrypt
import subprocess
from sanitizeInput import sanitize

def uphfSecure(zs):
    hashed = bcrypt.hashpw(zs.encode(), bcrypt.gensalt())
    return hashed


#hash and change password
def cup(n):
    stized = sanitize(n)
    pwHash = bcrypt.hashpw(stized.encode(),bcrypt.gensalt())
    with open("upf.txt","wb") as d:
        d.write(pwHash)
        d.close()

#change username
def cuu(n):
    stized = sanitize(n)
    unameHash = bcrypt.hashpw(stized.encode(),bcrypt.gensalt())
    with open("uuf.txt","wb") as d:
        d.write(unameHash)
        d.close()

#validate password
def vup(p):
    hn = p.encode()
    with open("upf.txt","rb") as d:
        osop = d.read()
        d.close()
        if(bcrypt.checkpw(hn,osop)):
            return True
    return False

#validate username
def vuu(u):
    hn = u.encode()
    with open("uuf.txt","rb") as d:
        osop = d.read()
        d.close()
        if(bcrypt.checkpw(hn,osop)):
            return True
    return False
