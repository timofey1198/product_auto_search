
# -*- coding: utf-8 -*-
import random
import time
from threading import Thread
from auto_test import get_str_time


class MyThread(Thread):
    """
    A threading example
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
        f = open('%s.txt' % self.name, 'w+')
        f.write(get_str_time()+'\n')
        f.write(str(time.time()))
        f.close()
    
def create_threads():
    """
    Создаем группу потоков
    """
    for i in range(5):
        name = "Thread %s" % (i+1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_threads()