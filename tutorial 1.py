from flask import Flask
from waitress import serve 

app = Flask(__name__)

@app.route("/")

def home():
    return "This is Nick's flask page"

if __name__=="__main__":
    serve(app, host="0.0.0.0", port=8000)