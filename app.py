from flask import Flask, app, request
import requests


app = Flask(__name__)
#https://api.telegram.org/bot1717938340:AAFr7fwkyg94ZWi0vOcJ-yErL8JB4NzfN4M/setWebhook?url=https://belle-gerard-08161.herokuapp.com/

TOKEN = '1717938340:AAFr7fwkyg94ZWi0vOcJ-yErL8JB4NzfN4M'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'text': message_text}

    return message

def send_message(chat_id, text='Введите лошин'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']

    if '/Start' in text:
        send_message(chat_id, 'Введите логин')

    if 'Login' in text:
        send_message(chat_id, 'Введите пароль')

    if 'Pass' in text:
        send_message(chat_id, 'ok')

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
    return {"ok": True}

    
if __name__ == '__app__':
    app.run()
