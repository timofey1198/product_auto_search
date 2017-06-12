# -*- coding: utf-8 -*-
import requests
import auto_test
import avito_html_parse

access_token = '389357078:AAG4b2zaoc-8bz4QU0gvwU5CZiUSZ38bpGo'


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
            token = access_token,
            method = 'sendMessage', 
            chat = chat_id, 
            text = message)
    r = requests.post(url)

def get_updates():
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token = access_token,
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
    print('Бот начал работу\n')
    while True:
        text, message_id, chat, user = get_last_message()
        if text == None:
            continue
        if message_id == get_num():
            continue
        else:
            if text == '/start' or text == '/new_search':
                message = 'Добро пожаловать в программу автоматического \
                поиска товаров и получения новейшей информации о них.'
                send_message(chat, message)
                message = 'Введите адрес ссылки для начала поиска:'
                send_message(chat, message)
                set_num(message_id)
                
                last_user = user
                text, message_id, chat, user = get_last_message()
                while True:
                    if message_id == get_num():
                        text, message_id, chat, user = get_last_message()
                        continue
                    else: break
                print(text)
                url = text
                #if not is_valid_url(url):
                    #while not is_valid_url(url):
                        #url = input('Неверный адрес. Повторите ввод:\n')
                
                r = auto_test.request_url(url)
                if not r:
                    send_message(chat, 'Продукт не найден')
                    set_num(message_id)
                else:
                    items = avito_html_parse.get_items('answer.html')
                    last_item = avito_html_parse.get_last_item_info(items)
                    message = last_item[0] + '\n' + last_item[1]
                    send_message(chat, message)
                    set_num(message_id)
                    message = 'Начат поиск...\nЧтобы выйти введите команду\
                    /close_search'
                    send_message(chat, message)
                    set_num(message_id)
                    while True:
                        text, message_id, chat, user = get_last_message()
                        if text == '/close_search':
                            set_num(message_id)
                            message = 'Для нового поиска введите /new_search'
                            send_message(chat, message)
                            set_num(message_id)
                            break
                        new_items = avito_html_parse.get_items('answer.html')
                        new_last_item = avito_html_parse.get_last_item_info(new_items)
                        if new_last_item == last_item:
                            continue
                        else:
                            items = new_items
                            last_item = new_last_item
                            message = last_item[0] + '\n' + last_item[1]
                            send_message(chat, message)
                            set_num(message_id)
            else:
                message = 'Hello, {name}!'.format(name = user)
                set_num(message_id)
                send_message(chat, message)


if __name__ == '__main__':
    start()