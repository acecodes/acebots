# Basic page opener template
from selenium import webdriver

entry = input('Please enter the name of a Wikipedia article: ')

entry = entry.replace(' ', '_')
entry = entry.strip()

browser = webdriver.Firefox()
browser.get('https://en.wikipedia.org/wiki/{entry}'.format(entry=entry))
assert "Wikipedia, the free encyclopedia" in browser.title()

browser.close()