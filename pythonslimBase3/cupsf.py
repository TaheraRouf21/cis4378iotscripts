import subprocess
import hashlib

#module for storing and comparing password


def uphf(z):
    hz = hashlib.sha256(z.encode())
    return hz.hexdigest()
    
#hash and change password
def cup(n):
    sfpd = uphf(n)
    cmmd = "echo'" + sfpd
    cmmd+="'| tee -a upf.txt" 
    result = subprocess.run([cmmd])

#change username
def cuu(n):
    cmmd = "echo '" + n
    cmmd+="' | tee -a uuf.txt" 
    result = subprocess.run([cmmd])

#validate password
def vup(p):
    hn = uphf(p)
    result = subprocess.run(["cat upf.txt"])
    osop = result.stdout.decode()
    if(hn==osop):
        return True
    return False

#validate username
def vuu(u):
    if(u):
