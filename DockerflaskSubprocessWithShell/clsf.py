import subprocess

#find active sessions
def validateUser(sessionKey):
    result = subprocess.run(["cat user.txt"], capture_output=True)
    op = result.stdout.decode()
    rslArr = op.split("\n")
    for usid in rslArr:
        if usid == sessionKey:
            return True
    return False 

def 


    