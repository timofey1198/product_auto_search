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

def new_user(chat_id, link):
    pass

def update_link(chat_id, new_link):
    pass

def new_status(chat_id, status):
    '''
    Change link status
    available statuses: {'work', 'closed', 'found'}
    '''
    pass


if __name__ == '__main__':
    #print(help(main_search_bot))
    pass