import requests
from lxml import html

custom_headers = {'user-agent': 'james-bond'}
page = requests.get('https://en.wikipedia.org/wiki/Monty_Python', headers=custom_headers)
tree = html.fromstring(page.text)

intro = tree.xpath('//*[@id="mw-content-text"]/p[1]/text()')

print(intro)