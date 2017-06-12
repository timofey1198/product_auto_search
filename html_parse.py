import lxml.html as html

page = html.parse('answer.html')

items_all = page.getroot().find_class('js-catalog_before-ads').pop()
items = items_all.getchildren()

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
    
print(last_item_title)
print(last_item_link)