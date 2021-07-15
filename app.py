from flask import Flask, app, request, jsonify
import requests
import json

app = Flask(__name__)

URL = 'https://api.telegram.org/bot1717938340:AAFr7fwkyg94ZWi0vOcJ-yErL8JB4NzfN4M/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='Введите лошин'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        if '/Start' in message:
            send_message(chat_id, text='Введите логин')

        return jsonify(r)
    return '<h1>privetik</h1>'

if __name__ == '__app__':
    app.run()
