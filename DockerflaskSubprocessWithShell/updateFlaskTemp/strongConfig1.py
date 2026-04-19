from flask import Flask, request, session, redirect, send_file, make_response, url_for
from home import getHome
from connectionPage import connPage
from gethtml import gethtml
import subprocess
import ssl
import uuid
import cupSecure
import usSessionWrite
from datetime import datetime, timedelta
from dateutil import parser
import FileManager

app = Flask(__name__)

def getSessionInfo():
    sessionuid= None
    with open("session.txt", "r") as f: 
        sessionuid = f.read()
        f.close()
    with open("sessionTime.txt","r") as z:
        lTime = z.read()
        z.close()
    loginTime = None
    if(lTime!=""):
        loginTime = parser.parse(lTime)
    return sessionuid,loginTime

def getSE():
    return timedelta(minutes=2)


def checkUser(retPage):
    user_id = request.cookies.get("uuid")
    if (user_id is None):
        print("no user id")
        return redirect(url_for("login"))
    if(not loggedIn()):
        return redirect(url_for("login"))
    return make_response(retPage)


def loggedIn():
    suidMatch = usSessionWrite.checkSession(request.cookies.get("uuid"))
    lgTime = parser.parse(usSessionWrite.getLT())
    if(lgTime is not None):
        print("loginTime: "+str(lgTime))
        timeSince = datetime.now()-lgTime
        print("timeSince: "+str(timeSince))
        if (timeSince>getSE()):
            print("timeSince is greater than sessionExpiration: ")
        print(suidMatch)
        if(suidMatch and timeSince<getSE()):
            return True
    return False


def validateLogin(pword, uname):
    print(" ")
    print("v login")
    print(" ")
    if(cupSecure.vup(pword) and cupSecure.vuu(uname)):
        print("valid login")
        usSessionWrite.writeSessionID(request.cookies.get("uuid"))
        usSessionWrite.writeLoginTime(str(datetime.now()))
        return True
    return False

def homeOrLogin():
    if loggedIn():
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))

def getLogin():
    return gethtml("login.html")

def postLogin():
    password = request.form["password"]
    uname = request.form["username"]
    if(validateLogin(password, uname)):
        print("valid login")
        return redirect(url_for("home"))
    return make_response(gethtml("loginIncorrect.html"))
    
@app.post("/connection")
def connection_post():
    return checkUser(connPage("connected"))

@app.get("/connection")
def connection():
    return checkUser(connPage(None))

@app.get("/")
def rootPath():
    return homeOrLogin()

@app.get("/home")
def home():
    return checkUser(getHome())

@app.post("/chusername")
def homePost():
    FileManager.fileWrite("password.txt", request.form["username"])
    return getHome()

@app.get("/login")
def login():
    user_id = request.cookies.get("uuid")
    if (user_id is None):
        new_id = uuid.uuid4()
        response = make_response(getLogin())
        response.set_cookie("uuid", new_id.hex)
        return response
    return gethtml("login.html")

@app.get("/camera")
def camera():
    if(loggedIn()):
        return send_file("fakecam.jpg", mimetype="image/jpg")
    return redirect(url_for("login"))

@app.post("/login")
def login_post():
    return postLogin()
    
if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("cert/lhcert.pem","cert/localhost.pem")
    app.run(ssl_context=context,host="0.0.0.0", port=5000)

