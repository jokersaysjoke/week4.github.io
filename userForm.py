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
        session["message"] = "請輸入帳號或密碼"
        return redirect(url_for("error", message = "請輸入帳號或密碼"))
    else:
        session["message"] = "帳號或密碼錯誤"
        return redirect(url_for("error", message = "帳號或密碼錯誤"))

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
        error = session["message"]
        return render_template("error.html",errorMessage = error)

app.run(port=3000)