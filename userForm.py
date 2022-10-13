from flask import Flask, request, redirect, render_template, session

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
    elif userName == '' :
        return redirect("/error2")
    elif passWord == '' :
        return redirect("/error2")
    else:
        return redirect("/error")

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
        errorMessage = request.args.get("message", "帳號或密碼輸入錯誤")
        return render_template("error.html", error=errorMessage)

@app.route("/error2", methods=["GET"])
def error2():
    errorMessage = request.args.get("message","請輸入帳號、密碼")
    return render_template("error2.html", error=errorMessage)

app.run(port=3000)