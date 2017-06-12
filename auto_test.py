# -*- coding: utf-8 -*- 
import requests
import time
import avito_html_parse

avalible_urls = ['http://avito.ru', 'http://www.avito.ru']

def is_valid_url(url):
    for u in avalible_urls:
        if u in url:
            if url.index(u) == 0:
                return True
    return False

def get_str_time():
    year = time.gmtime(time.time())[0]
    month = time.gmtime(time.time())[1]
    day = time.gmtime(time.time())[2]
    hour = time.gmtime(time.time())[3]
    minute = time.gmtime(time.time())[4]
    sec = time.gmtime(time.time())[5]
    str_time = '{y}.{mon}.{d} {h}-{m}-{s}'.format(y = year, mon = month,
                                                  d = day, h = hour,
                                                  m = minute, s = sec)
    return str_time


def request_url(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\
        /537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        r = requests.post(url, data = {'User-Agent' : user_agent, 
                                       'Accept-Charset:' : 'ascii',
                                       'Accept-Language' : 'en'
                                       }
                          )
        
        log = open('log/search/%s.txt'%get_str_time(), 'w+')
        for key in r.headers:
            log.write('{k} : {v}\n'.format(k = key, v = r.headers[key]))
        log.close()
        
        f = open('answer.html', 'w+', encoding='utf-8')
        f.write(r.text)
        f.close()
    except:
        return False
    return True


if __name__ == '__main__':
    print('Программа запущена в консольном режиме.\n')
    
    url = input('Введите ссылку для поиска:\n')
    if not is_valid_url(url):
        while not is_valid_url(url):
            url = input('Неверный адрес. Повторите ввод:\n')
    
    r = request_url(url)
    if not r:
        print('Продукт не найден')
    else:
        items = avito_html_parse.get_items('answer.html')
        last_item =avito_html_parse.get_last_item_info(items)
        print(last_item[0])
        print(last_item[1])