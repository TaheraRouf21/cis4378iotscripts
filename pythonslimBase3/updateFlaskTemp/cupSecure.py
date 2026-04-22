import bcrypt
import subprocess

def uphfSecure(zs):
    hashed = bcrypt.hashpw(zs.encode(), bcrypt.gensalt())
    return hashed


#hash and change password
def cup(n):
    pwHash = bcrypt.hashpw(n.encode(),bcrypt.gensalt())
    cmmd = "/bin/rbash -c \""
    cmmd += "echo'" + pwHash.decode()
    cmmd+="'| tee upf.txt\"" 
    result = subprocess.run([cmmd])

#change username
def cuu(n):
    unameHash = bcrypt.hashpw(tpw.encode(),bcrypt.gensalt())
    cmmd = "/bin/rbash -c \""
    cmmd += "echo '" + unameHash.decode()
    cmmd+="' | tee uuf.txt\"" 
    result = subprocess.run([cmmd])

#validate password
def vup(p):
    hn = p.encode()
    result = subprocess.run(["/bin/rbash -c \"cat upf.txt\""],shell=True,capture_output=True)
    osop = result.stdout.decode()
    osop = osop.strip()
    if(bcrypt.checkpw(hn,osop.encode())):
        return True
    return False

#validate username
def vuu(u):
    hn = u.encode()
    result = subprocess.run(["/bin/bash -c \"cat uuf.txt\""],shell=True,capture_output=True)
    osop = result.stdout.decode()
    osop = osop.strip()
    if(bcrypt.checkpw(hn,osop.encode())):
        return True
    return False
