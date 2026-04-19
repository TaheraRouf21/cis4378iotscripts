def connPage(status):
    connection = """<html>
<style>

    body {
        background-color: #9ABDDC;
        padding: 0rem 5rem 0rem 5rem;
    }

    .page {
        background-color:#BEBEBE;
        height:40rem;
        margin:auto;
        padding-left:4rem;
    }

    .content{
        background-color: #808080;
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

    .selectedPage{
        background-color: #949494;
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
    <div class="navbar">
        <div class="navlinks">
            <div class="navlink"><a href="/home">home</a></div>
            <div class="navlink selectedPage"><a href="/connection">Connection</a></div>
        </div>
    </div>
    <h2>current connection:</h2>
    <p>"""
    
    connection += "put connection info command"

    connection += """</p>
    <br/>
    <h3>Connect to a network:</h3>
    <form action='#' class="form" method='post'>
     <p>ssid:</p><br>
     <input type='text' name='username'></input>
     <p>password:</p><br>
     <input type='text' name='password'></input>
     <input type='submit' class="submit"></input>
     </form>"""
    if (status is not None):
        if status == 0:
            connection +="<h2>Connected to new network</h2>"
        else:
            connection +="<h2>Error, please try again</h2>"

    connection += """</div>
</body>

</html>
"""
    return connection
