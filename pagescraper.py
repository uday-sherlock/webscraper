# link scraper from http://en.wikipedia.org/wiki/Lists_of_diseases
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
page1 = "http://en.wikipedia.org/wiki/List_of_cancer_types"
page = "http://en.wikipedia.org/wiki/Lists_of_diseases"
shorttest = "http://www.kidsworldfun.com/shortstories_lionandmouse.php"
usetest = "http://en.wikipedia.org/wiki/Acute_lymphoblastic_leukemia"
parent_page = requests.get(page)
links = []
prefix ='http://en.wikipedia.org' 
#tags
btags = 'b'
htags = 'h'
tagl = 'ul'
tagtable = 'tbody'
ptags = 'p'
# atags = SoupStrainer("a") 
# p = parent_page.content
# view_page = BeautifulSoup(p,"html.parser",parse_only = atags)
# # print view_page.prettify()
# for link in view_page.find_all('a'):
# 	l = link.get('href')
# 	# print l
# 	try: 
# 		Link = prefix+l
# 		# print Link
# 	except TypeError:
# 		continue
# 	links.append(Link)

# print links[24:30]
# num = links.index('http://en.wikipedia.org/wiki/wiki/Acute_lymphoblastic_leukemia')
# num2 = links.index('http://en.wikipedia.org/wiki/wiki/Thyroid_cancer')
# print num,num2
# print links



def textscraper(webadd):
	data = []
	targetpage = requests.get(webadd)
	t = targetpage.content
	targetcontent = BeautifulSoup(t)
	# print targetcontent.prettify()
	LoT = targetcontent.find_all([btags,htags,ptags,tagl,tagtable])
	# print LoT
	for elem in LoT:
		data.append(elem.text)
	return data

ans = textscraper(usetest)
print ans