from flask import Flask, request
import subprocess

app = Flask(__name__)


login = """<html>
<style>

    body {
        background-color: #9ABDDC;
        padding: 0rem 5rem 0rem 5rem;
    }

    .page {
        background-color:#BEBEBE;
        height:20rem;
        margin:auto;
        padding-left:4rem;
    }

    .content{
        background-color: #808080;
    }


    .form{
        background-color:#DEDEDE;
        height:14rem;
        width:12rem;
        padding-left:0.8rem;
    }

    .submit{
        margin-top:1rem;
    }

</style>
<body>
    <div class="page">
    <form action='#' class="form" method='post'>
     <p>username:</p><br>
     <input type='text' name='username'></input>
     <p>password:</p><br>
     <input type='text' name='password'></input>
     <input type='submit' class="submit"></input>
     </form>

</div>
</body>

</html>"""

login_incorrect = """<html>
<style>

    body {
        background-color: #9ABDDC;
        padding: 0rem 5rem 0rem 5rem;
    }

    .page {
        background-color:#BEBEBE;
        height:20rem;
        margin:auto;
        padding-left:4rem;
    }

    .content{
        background-color: #808080;
    }


    .form{
        background-color:#DEDEDE;
        height:14rem;
        width:12rem;
        padding-left:0.8rem;
    }

    .submit{
        margin-top:1rem;
    }

</style>
<body>
    <div class="page">
    <h2>Incorrect username or password</h2>
    <form action='#' class="form" method='post'>
     <p>username:</p><br>
     <input type='text' name='username'></input>
     <p>password:</p><br>
     <input type='text' name='password'></input>
     <input type='submit' class="submit"></input>
     </form>

</div>
</body>

</html>"""

def getTime():
    form ="<form action='#' method='post'>"
    form += "Time: <input type='time' name='inputTime'></input><br>"
    form +="Date: <input type='date' name='inputDate'></input>"
    form +="<input type='submit'>Save</input>"
    return form

def setTime():
    time = request.form["time"]
    date = request.form["date"]
    page = "<div>"+time+"<br>"+date+"</div>"
    return page
    

def getLogin():
    return login

def postLogin():
    password = request.form["password"]
    uname = request.form["username"]
    subprocess.run([""])
    return login_incorrect

@app.get("/time")
def home():
    return setTime()

@app.post("/time")
def time_post:
    return setTime()

@app.get("/home")
def login():
    return getLogin()

@app.post("/home")
def login_post():
    return postLogin()

@app.post("/home/changepassword")
def 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

