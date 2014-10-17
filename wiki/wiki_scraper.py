import os
import urllib.request
import time
from datetime import datetime, date
from re import findall, sub
from bs4 import BeautifulSoup
import os
from flask import Flask, render_template

app = Flask(__name__)

class WikiScrape:

	def __init__(self, url):
		self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
		self.url = "http://en.wikipedia.org/wiki/" + url
		self.req = urllib.request.Request(self.url, headers=self.header)
		self.data = urllib.request.urlopen(self.req)
		self.soup = BeautifulSoup(self.data)
		self.body = self.soup.get_text()
		self.infoboxes = self.soup.find_all('table', {"class":"infobox"})
		self.text = self.soup.find_all('p')

	def regex(self, string):
		return findall(string, self.body)

@app.route('/')
def index():
	Neuron = WikiScrape('Neuron') # Test with Neuron Wikipedia page
	info = Neuron.infoboxes
	text = Neuron.text
	return render_template('index.html', info=info, text=text, len=len)	

if __name__ == '__main__':
	app.run(debug=True)