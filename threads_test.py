
# -*- coding: utf-8 -*-
import random
import time
from threading import Thread
from auto_test import get_str_time
import main_search_bot
import data


class LinkSerfer(Thread):
    """
    Thread to serf links.db and
    send updates for users
    """
    
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        """Запуск потока"""
        amount = random.randint(3, 3)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)
        #
        # Тут оснвная работа программы
        while True:
            working_users = data.get_users_info('work')
            for user in working_users:
                link = user[3]
                answer = user[4]
                new_answer = main_search_bot.get_link_answer(link)
                if answer != new_answer:
                    num = user[0]
                    chat_id = user[1]
                    data.set_answer(num, new_answer)
                    main_search_bot.send_message(chat_id, new_answer)
                time.sleep(61)
        #
    
def create_threads():
    """
    Создаем группу потоков
    """
    for i in range(1):
        name = "Thread %s" % (i+1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    print(main_search_bot.access_token)