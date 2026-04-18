def getHome(n):
    home = """<html>
<style>

    body {
        background-color: #9ABDDC;
        padding: 0rem 5rem 0rem 5rem;
    }

    .page {
        background-color:#BEBEBE;
        height:50rem;

    }

    .navbar{
        background-color: #949494;

    }

    .navlinks {
        display:flex;
        flex-direction: row;
        padding-left:5rem;
    }
    
    .navlink{
        padding:1rem 1rem 1rem 1rem;
        margin:1rem 0rem 1rem 0rem;
        background-color: white;
        border:0.1rem solid #0F0F0F;

    }

    .content{
        background-color: #808080;
    }

    .selectedPage{
        background-color: #949494;
    }
    
    h3{
        margin-left:20rem;
    }

    .camVP{
        height:20rem;
        margin-left:20rem;
    }

</style>
<body>
    <div class="page">
    <div class="navbar">
        <div class="navlinks">
            <div class="navlink selectedPage"><a href="/home">home</a></div>
            <div class="navlink"><a href="/connection">Connection</a></div>
        </div>
    </div>
    <div> """
    home +=n
    home+="""
        <h3>Hello</h3>
    </div>
    <h3>Live feed:</h3>
    <img class="camVP" src="/camera"></img>
    <br/>
    <br/>
    <form action="/home/changeusername" method="post">
    new username: <input name="username"></input>
    <input type="submit"></input>
    </form>
    <form action="/home/changepassword" method="post">
    new password: <input name="password"></input>
    <input type="submit"></input>
    </form>
</div>
</body>
</html>
"""
    return home