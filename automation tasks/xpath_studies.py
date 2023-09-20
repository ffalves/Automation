from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/Zwan')
tree = html.fromstring(page.content)

# # how many DIV are it has inside the BODY
# divs = tree.xpath('/html/body/div')
# print(len(divs)) #3 but in the inspection on page we can see 5 divs | I can't understand why it didn't find 2+ divs, I think they are unvailable or empty
# print(divs)
# print(divs)

# # how many DIV are with some CLASS
# div_class = tree.xpath('/html/body/div/@class')
# print(len(div_class)) #3 ['vector-header-container', 'mw-page-container', 'vector-settings']
# print(div_class)

# # how many DIV are with some ID
# div_id = tree.xpath('/html/body/div/@id')
# print(len(div_id)) #1 ['p-dock-bottom'] | I can't understand why it didn't find 2+ divs, I think they are unvailable or empty
# print(div_id)

# # how many SPAN it has regardless of location
# span = tree.xpath('//span')
# print(len(span)) #313
# print(span)

# # how many TABLE it has regardless of location
# table = tree.xpath('//table')
# print(len(table)) #5
# print(table)

# how many TABLE it has regardless of location
# table_1st = tree.xpath('//table[1]')
# print(len(table_1st)) #5
# print(table_1st)

# how many TABLE it has regardless of location
table_1st = tree.xpath('//h1')
print(len(table_1st)) #5
print(table_1st)