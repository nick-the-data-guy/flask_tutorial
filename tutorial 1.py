from flask import Flask

app = Flask(__main__)

def home():
    return "This is Nick's flask page"

if __name__=="__main__":
    app.run()