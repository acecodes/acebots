# Script for pulling information about 

from bs4 import BeautifulSoup
import urllib.request

class User:
	def __init__(self, username):
		self.username = username
		self.url = urllib.request.urlopen('https://www.github.com/{user}'.format(user=self.username))
		self.soup = BeautifulSoup(self.url)
		self.body = self.soup.get_text()

	def commit_streak(self):
		return self.soup.find_all('div', {'class':'contrib-details'})

if __name__ == '__main__':
	AceCodes = User('acecodes') # Using my username as a test
	print(AceCodes.commit_streak())