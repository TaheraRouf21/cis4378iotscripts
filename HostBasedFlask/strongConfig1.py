from flask import Flask, request, session, redirect, send_file, make_response, url_for
from home import getHome
from connectionPage import connPage
from gethtml import gethtml
import subprocess
import ssl
import uuid
import cupSecure
from datetime import datetime, timedelta
from dateutil import parser
import usSessionWrite

app = Flask(__name__)

def checkUser(retPage):
    user_id = request.cookies.get("uuid")
    if (user_id is None):
        print("no user id")
        return redirect(url_for("login"))
    if(not loggedIn()):
        return redirect(url_for("login"))
    return make_response(retPage)


def loggedIn():
    sCheck = usSessionWrite.checkSession(request.cookies.get("uuid"))
    tCheck = usSessionWrite.checkLoginTime()
    if(sCheck & tCheck):
            return True
    return False


def validateLogin(pword, uname):
    if(cupSecure.vup(pword) and cupSecure.vuu(uname)):
        usSessionWrite.writeID(request.cookies.get("uuid"))
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
    userIP = request.remote_id
    if(usSessionWrite.checkAttemptCount(userIP)):
        password = request.form["password"]
        uname = request.form["username"]
        if(validateLogin(password, uname)):
            usSessionWrite.resetAttemptCount(userIP)
            return redirect(url_for("home"))
        usSessionWrite.addLoginAttempt(userIP)
        usSessionWrite.WriteLogTime(userIP)
        if(usSessionWrite.checkAttemptCount(userIP)):
            return "<h3>Too many attempts max is 2: locked for 1 minute</h3>"
        return make_response(gethtml("loginIncorrect.html"))
    return("<h3>Too many attempts max is 2: locked for 1 minute</h3>")
    
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
    return checkUser(getHome(""))

@app.post("/home/changeusername")
def chUname():
    cupSecure.cuu(request.form["username"])
    return getHome("<h2>changed username</h2>")

@app.post("/home/changepassword")
def chPwd():
    cupSecure.cup(request.form["password"])
    return getHome("<h2>changed password</h2>")

@app.get("/login")
def login():
    user_id = request.cookies.get("uuid")
    if (user_id is None):
        new_id = uuid.uuid4()
        response = make_response(getLogin())
        response.set_cookie("uuid", new_id.hex)
        return response
    if(usSessionWrite.checkAttemptCount(request.cookies.get("uuid"))):
        return gethtml("login.html")
    return ("<h3>Too many login attempts: Max Login Attempts 2</h3>")

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

