from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "This is Nick's flask page"

if __name__=="__main__":
    app.run()