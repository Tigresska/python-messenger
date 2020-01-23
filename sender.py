import requests

response = requests.get("http://127.0.0.1:5000/status")
print(response.text)

username = input("Введите ваше имя: ")
password = input("Введите пароль: ")
response = requests.post(
    "http://127.0.0.1:5000/auth",
    json={"username": username, "password": password}
)
if not response.json()['ok']:
    print("Неверный пароль!!!")
else:
    while True:
        text = input("Введите сообщение: ")
        response = requests.post(
            "http://127.0.0.1:5000/send",
            json={"username": username, "password": password, "text": text}
        )
# print(response.text)

# "/send"
# {"username": "", "text": ""}
