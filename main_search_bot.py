# -*- coding: utf-8 -*-
import requests
import time
import random
import auto_test
import avito_html_parse
from os.path import dirname, realpath
import data

main_path = dirname(realpath(__name__))
access_token = '389357078:AAG4b2zaoc-8bz4QU0gvwU5CZiUSZ38bpGo'


def get_num():
    f = open(main_path + '/data/settings', 'r')
    N = int(f.read())
    return N

def set_num(n):
    f = open(main_path + '/data/settings', 'w+')
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
    '''
    Get all updates for this bot
    '''    
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token = access_token,
        method = 'getUpdates')
    r = requests.post(url)
    if r.json()['ok']:
        return r.json()['result']
    else:
        return 'Error!'


def get_link_answer(link):
    r = auto_test.request_url(link)
    if r:
        items = avito_html_parse.get_items(main_path + '/data/answer.html')
        if items == None:
            return 'Ничего не найдено'
        last_item_info = avito_html_parse.get_last_item_info(items)
        if last_item_info == None:
            return 'Ничего не найдено'
        last_item_title, last_item_link = last_item_info
        answer = last_item_title + '\n' + last_item_link
        return answer
    else:
        return 'Неверный адрес'


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
        # Получаем последнее принятое сообщение
        text, message_id, chat, user = get_last_message()
        if text == None:
            continue
        if message_id == get_num():
            continue
        else:
            # Проверка на существование пользователя
            if not data.is_exist_user(chat):
                # Добавляем в базу нового пользователя
                data.new_user(chat, '', '', 'closed')
                
            if text == '/start' or text == '/new_search':
                message = 'Добро пожаловать в программу автоматического \
                поиска товаров и получения новейшей информации о них.'
                send_message(chat, message)
                message = 'Введите адрес ссылки для начала поиска:'
                send_message(chat, message)
                set_num(message_id)
                data.set_status(chat, 'ready')              
                
            elif auto_test.is_valid_url(text):
                num = data.get_num(chat)
                status = data.get_status(num)
                if status == 'ready':
                    data.set_link(chat, text)
                    data.set_status(chat, 'work')
                    # Тут добавить поиск и добавление 
                    # ответа по ссылке
                    answer = get_link_answer(text)
                    send_message(chat, answer)
                    set_num(message_id)
                    data.set_answer(num, answer)
                    
                elif status == 'work':
                    message = 'В данное время уже ведется поиск.\n\
                    Для нового поиска введите команду /new_search'
                    send_message(chat, message)
                    set_num(message_id)
                else:
                    message = """Поиск еще не начат.\n
                    Для нового поиска введите команду /new_search"""
                    send_message(chat, message)
                    set_num(message_id)
                    
            elif text == '/close_search':
                # Прописать изменение статуса ссылки в базе
                pass
            
            else:
                message = 'Hello, {name}!'.format(name = user)
                set_num(message_id)
                send_message(chat, message)


if __name__ == '__main__':
    start()
    #print(get_link_answer('http://www.avito.ru/moskva?q=kawasaki+kle+250'))