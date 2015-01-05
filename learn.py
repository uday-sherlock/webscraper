import requests
from bs4 import BeautifulSoup
testpage = 'http://en.wikipedia.org/wiki/Acute_lymphoblastic_leukemia'
shorttest = 'http://www.kidsworldfun.com/shortstories_lionandmouse.php'
btags = 'b'
htags = 'h'
tagl = 'ul'
tagtable = 'tbody'
ptags = 'p'
# page = requests.get(testpage)
# c = page.content
# p = BeautifulSoup(c)
# total = p.find_all('a')
# print type(total)
# for l in total:
# 	single =  l.get('href')
# 	text = l.text
# print type(single),type(text)


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


rawdata = textscraper(shorttest)
# print text

def datadelimiterandstriper(scraperdata):
	sentences = []
	delimited = []
	for data in scraperdata:
		delimited = data.split('.')
		for sentence in delimited:
			sentences.append(sentence.strip('\n'))
	return sentences

textlist = datadelimiterandstriper(rawdata)
# print textlist

def blanklinerem(delimstripdata):
	d = delimstripdata
	b = ''
	blankpresent = True
	while(blankpresent):
		try: idx = d.index(b)
		except ValueError:
			return d
		else:
			d.remove(b)
	return d


usefullist = blanklinerem(textlist)
# print usefullist

def shortsenrem(blankremdata):
	b = blankremdata
	for sen in b:
		if len(sen)<=5:
			b.remove(sen)
	return b


meaningfullist = shortsenrem(usefullist)
print meaningfullist


