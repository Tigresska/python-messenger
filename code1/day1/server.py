from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, <h1>World</h1>!"


@app.route("/status")
def status():
    return {
        "status": True,
        'time': datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    }


app.run()