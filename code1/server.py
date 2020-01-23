from datetime import datetime, time
from flask import Flask, request

app = Flask(__name__)
messages = [
    {"username": "Jack", "text": "Hello!", "time": time.time()},
    {"username": "Mary", "text": "Hi, Jack!", "time": time.time()},
]

@app.route("/")
def hello():
    return "Hello, <h1>Welcom ti Python meessenger!</h1>!"


@app.route("/status")
def status():
    return {
        "status": True,
        'time': datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    }

@app.route("/send")
def send():
    data = request.json()
    username = data["username"]
    text = data["text"]

    messages.append({"username": username, "text": text, "time": time.time()},)

    return {'ok': True}



app.run()