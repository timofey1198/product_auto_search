
# -*- coding: utf-8 -*-
import random
import time
from threading import Thread
from auto_test import get_str_time
import main_search_bot


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