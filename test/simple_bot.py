import requests

def get_num():
    f = open('settings', 'r')
    N = int(f.read())
    return N

def set_num(n):
    f = open('settings', 'w+')
    f.write(str(n))
    f.close()

def send_message(chat_id, message):
    url = 'https://api.telegram.org/bot{token}/{method}?chat_id={chat}&text={text}'.format(
            token = '384020723:AAHwwNlP0AiWWXpyND2rNr7zc9mPe9YM3kU',
            method = 'sendMessage', 
            chat = chat_id, 
            text = message)
    r = requests.post(url)

def get_updates():
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token = '384020723:AAHwwNlP0AiWWXpyND2rNr7zc9mPe9YM3kU',
        method = 'getUpdates')
    r = requests.post(url)
    if r.json()['ok']:
        return r.json()['result']
    else:
        return 'Error!'

def get_last_message():
    results = get_updates()
    if bool(results):
        res = results[-1]
        message = res['message']
        text = message['text']
        message_id = message['message_id']
        chat_id = message['chat']['id']
        user = message['chat']['first_name']
        return (text, message_id, chat_id, user)
    else:
        return (None, None, None, None)

def start():
    while True:
        text, message_id, chat, user = get_last_message()
        if text == None:
            continue
        if message_id == get_num():
            continue
        else:
            print(text)
            set_num(message_id)
            send_message(chat, 'Hello, {name}!'.format(name = user))


if __name__ == '__main__':
    #for m in get_updates():
        #print(m)
    #print(get_last_message())
    start()