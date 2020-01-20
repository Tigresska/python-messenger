from time import strftime, localtime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, <h1>World</h1>!"


@app.route("/status")
def status():
    return {
        "status": 'True',
        'time': strftime("%H:%M:%S %d.%m.%Y", localtime())
    }


app.run()
