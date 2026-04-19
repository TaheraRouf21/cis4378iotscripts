import subprocess;


def fileRead(file):
    with open(file+".txt","r") as d:
        temp = d.read()


def fileWrite(file, wString):
    with open(file+".txt", "w") as d:
        d.write(wString)
        d.close()
        

def writeBytes(file, wString):
    with open(file+".txt","wb") as d:
        d.write(wSrtring)
        d.close()