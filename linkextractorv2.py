import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

atags = SoupStrainer("a") 

parent_page = requests.get("http://en.wikipedia.org/wiki/Lists_of_diseases")
parent_add = "http://en.wikipedia.org/wiki/Lists_of_diseases"
prefix ='http://en.wikipedia.org' 

def link_scraper(webadd):
	links = []
	target_page = requests.get(webadd)
	p = target_page.content
	view_page = BeautifulSoup(p,"html.parser",parse_only = atags)
	print view_page.prettify()
	for link in view_page.find_all('a'):
		l = link.get('href')
		try: Link = prefix+l
		except TypeError:
			continue
		links.append(Link)
	# return links

print link_scraper(parent_add)