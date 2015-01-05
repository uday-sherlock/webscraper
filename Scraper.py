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
	# print view_page.prettify()
	for link in view_page.find_all('a'):
		l = link.get('href')
		try: Link = prefix+l
		except TypeError:
			continue
		links.append(Link)
	return links

def getfirstlinks(parent_add):
	links = link_scraper(parent_add)
	nxt_links = links[links.index('http://en.wikipedia.org/wiki/List_of_cancer_types'):links.index('http://en.wikipedia.org/wiki/List_of_cancer_types')+6]
	return nxt_links



def getsecondlinks(sec_add):
	target = sec_add
	links = link_scraper(target)
	# print links
	useful_links = links[24:177+1]
	return links

def getallsecondlinks(level):
	dic = {}
	for link in level:
		# print link
		dic[link] = getsecondlinks(link)
	return dic



level1 = getfirstlinks(parent_add)
# print level1
l2dic = getallsecondlinks(level1)
# print l2dic
# for key in l2dic:
# 	print key
# print l2dic['http://en.wikipedia.org/wiki/List_of_cancer_types']


# def textscraper(webadd):
# 	targetpage = requests.get(webadd)
# 	t = targetpage.content
# 	targetcontent = BeautifulSoup(t)
# 	final = targetcontent.get_text()
# 	return final

# links to look out for <ul> <p> <b> <tbody> <h>
btags = 'b'
htags = 'h'
tagl = 'ul'
tagtable = 'tbody'
ptags = 'p'

ALLLINKS = []
for key in l2dic:
	for string in l2dic[key]:
		ALLLINKS.append(string)

def linkstofile(links):
	nameHandle = open('Linkextracted.txt','w')
	for link in links:
		nameHandle.write(link)
		nameHandle.write('\n')
	nameHandle.close()

linkstofile(ALLLINKS)


# def loaddata(links):
# 	pagedata = {}
# 	for link in links:
# 		pagedata[link] = textscraper(link)
# 	return pagedata


# pagedata = loaddata(ALLLINKS)

# def reformatdata(dic):
# 	newdic = {}
# 	for key in dic.keys():
# 		newdic[key] = dic[key].split('.')
# 	return newdic

# dotsepdata = reformatdata(pagedata)
# print dotsepdata.keys()
