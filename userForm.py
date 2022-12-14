from flask import Flask, request, redirect, render_template, session,url_for

app=Flask(
    __name__,
    static_folder="static")

app.secret_key="99tsmc"

@app.route("/")
def homePage():
    return render_template("logIn.html")

@app.route("/signin" ,methods=["POST"])
def signin():
    userName = request.form["id"]
    passWord = request.form["password"]
        
    if userName == "text" and passWord == "text":
        session["user"]=userName
        return redirect("/member")
    elif userName == '' or passWord == '':
        return redirect("/error?message=請輸入帳號、或密碼")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/signout")
def signout():
    session.pop("user", None)
    return redirect("/")


@app.route("/member")
def member():
    if "user" in session:
        return render_template("member.html")
    return redirect("/")

@app.route("/error" ,methods=["GET"])
def error():
    message = request.args.get("message")
    return render_template("error.html", errorMessage = message)

@app.route("/square/<integer>")
def square(integer):
    integer = int(integer)**2
    return render_template("square.html", ans = integer)

@app.route("/turnToSquare")
def turnToSquare():
    integer = request.args.get("integer")
    if integer == "":
        return redirect("/")
    else:
        return redirect(url_for("square", integer = integer ))

app.run(port=3000)