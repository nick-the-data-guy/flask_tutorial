from flask import Flask, redirect, url_for
from waitress import serve

app = Flask(__name__)



@app.route("/")
def home():
    return "This is Nick's flask page <h1> HELLO</h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))




if __name__=="__main__":
    serve(app, host="0.0.0.0", port=8000)