# -*- coding: utf-8 -*-
import lxml.html as html
from os.path import dirname, realpath

main_path = dirname(realpath(__name__))


def get_items(filename):
    try:
        page = html.parse(filename)
        items_all = page.getroot().find_class('js-catalog_before-ads').pop()
        items = items_all.getchildren()        
    except:
        return None
    return items

def get_last_item_info(items):
    try:
        last_item = items[0]
        last_item_content = last_item.getchildren()
        last_item_photo_container = last_item_content[0]
        last_item_description = last_item_content[2]
        last_item_header = last_item_description.getchildren()[0]
        last_item_title_conteiner = last_item_header.getchildren()[0]
        last_item_title = last_item_title_conteiner.text_content().strip()
        last_item_link_conteiner = last_item_title_conteiner.getchildren()[0]
        last_item_link = ''
        for a in last_item_link_conteiner.iterlinks():
            last_item_link = a[2]        
    except:
        return None
    return (last_item_title, 'https://avito.ru' + last_item_link)