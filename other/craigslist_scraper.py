import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

def parse_results(search_term):
	results = []
	search_term = search_term.strip().replace(' ','+')
	search_url = BASE_URL.format(search_term)
	soup = BeautifulSoup(urlopen(search_url).read())
	rows = soup.find('div', 'content').find_all('p', 'row')
	for row in rows:
		url = 'http://sandiego.craigslist.org' + row.a['href']
		create_date = row.find('span', 'date').get_text()
		title = row.find_all('a')[1].get_text()
		results.append({'url':url, 'create_date':create_date, 'title':title})

	return results

def write_results(results):
	fields = results[0].keys()
	with open('results.csv', 'w') as f:
		dw = csv.DictWriter(f, fieldnames=fields, delimiter='|')
		dw.writer.writerow(dw.fieldnames)
		dw.writerows(results)

def has_new_records(results):
	pass