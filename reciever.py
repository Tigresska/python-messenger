from datetime import datetime
import time

import requests

last_time = 0

while True:
    response = requests.get("http://127.0.0.1:5000/messages",
                            params={'after': last_time})
    messages = response.json()["messages"]
    for message in messages:
        time_formated = datetime.fromtimestamp(message["time"])
        time_formated = time_formated.strftime("%H:%M:%S %d.%m.%Y")
        print(f'{message["username"]} {time_formated}')
        print(f'{message["text"]}')
        print()

        last_time = message["time"]
    time.sleep(1)