# -*- coding: utf-8 -*-
from os.path import dirname, realpath
import sqlite3
import main_search_bot

main_path = dirname(realpath(__name__))


conn = sqlite3.connect(main_path + '/data/links.db')
cursor = conn.cursor()
 
# Создание таблицы
'''
cursor.execute("""CREATE TABLE links
                  (id integer primary key, chat_id integer, status text,
                   link text)
               """)
'''

def get_last_link_num():
    conn = sqlite3.connect(main_path + '/data/links.db')
    cursor = conn.cursor()
    sql = "SELECT MAX([id]) FROM links"
    cursor.execute(sql)
    return cursor.fetchall()[0][0]

def new_user(chat_id, link, status = 'work'):
    number = get_last_link_num()
    if number == None:
        number = 0
    number += 1
    conn = sqlite3.connect(main_path + '/data/links.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO links
                   VALUES (?, ?, ?, ?)
                   """, [str(number), str(chat_id), status, link])
    conn.commit()

def update_link(chat_id, new_link):
    conn = sqlite3.connect(main_path + '/data/links.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE links
    SET link=?
    WHERE chat_id=?
    """, [new_link, str(chat_id)])
    conn.commit()

def new_status(chat_id, status):
    '''
    Change link status
    available statuses: {'work', 'closed', 'found', 'test'}
    '''
    conn = sqlite3.connect(main_path + '/data/links.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE links
    SET status=?
    WHERE chat_id=?
    """, [status, str(chat_id)])
    conn.commit()

def get_link_info(num):
    last_num = get_last_link_num()
    if type(num) != int:
        return None
    if last_num == None:
        return None
    if num > last_num:
        num = 1
    conn = sqlite3.connect(main_path + '/data/links.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM links WHERE id=?
                   """, [("%i"%num)])
    return cursor.fetchall()[0]

def get_link(num):
    info = get_link_info(num)
    return info[3]

def get_status(num):
    info = get_link_info(num)
    return info[2]

def get_chat_id(num):
    info = get_link_info(num)
    return info[1]


if __name__ == '__main__':
    new_status(111111, 'test')
    print(get_link_info(1))
    #new_user(111111, 'http://test.test', 'test')
    #print(help(main_search_bot))
    #pass