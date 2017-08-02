from flask import Flask, redirect, render_template, session, url_for, request

app=Flask(__name__)
app.secret_key="xyz"

@app.route("/")
def index():
    return render_template("expense.html")

@app.route('/register', methods=["POST"])
def register():
    if request.form["flatowner"]=="" or request.form["expense"] =="":
        return render_template("failure.html")
    return render_template("success.html")
