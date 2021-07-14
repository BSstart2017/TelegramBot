import requests


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
    #d = get_updates()
   # with open('update.json', 'w') as file:
    #    json.dump(d, file, indent=2, ensure_ascii=False)
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']

    if '/Start' in text:
        send_message(chat_id, 'Введите пароль')

    
if __name__ == '__main__':
    main()
