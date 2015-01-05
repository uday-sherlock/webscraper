import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
page1 = "http://en.wikipedia.org/wiki/List_of_cancer_types"
page = "http://en.wikipedia.org/wiki/Lists_of_diseases"
testpage = "http://en.wikipedia.org/wiki/Acute_lymphoblastic_leukemia"
testpage2 = "http://en.wikipedia.org/wiki/Bladder_cancer"
testpage3 = "http://en.wikipedia.org/wiki/Gallbladder_cancer"
shorttest = 'http://www.kidsworldfun.com/shortstories_lionandmouse.php'
# parent_page = requests.get(page)
# links = []
prefix ='http://en.wikipedia.org' 

# links to look out for <ul> <p> <b> <tbody> <h>
btags = 'b'
htags = 'h'
tagl = 'ul'
tagtable = 'tbody'
ptags = 'p'

def makecontent(targetlink):
	targetpage = requests.get(targetlink)
	t = targetpage.content
	targetcontent = BeautifulSoup(t)
	filename = targetcontent.title.string
	# print filename
	rawdata = textscraper(targetlink)
	# print rawdata
	textlist = datadelimiterandstriper(rawdata)
	usefullist = blanklinerem(textlist)
	meaningfullist = shortsenrem1(usefullist)
	maketextfile(meaningfullist, filename)


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



def datadelimiterandstriper(scraperdata):
	sentences = []
	delimited = []
	for data in scraperdata:
		delimited = data.split('.')
		for sentence in delimited:
			sentences.append((sentence.strip('\n')).strip(' '))
	return sentences


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



# print usefullist

def shortsenrem1(blankremdata):
	b = blankremdata
	for sen in b:
		if len(sen.split(' '))<=4:
			b.remove(sen)
	return b




			

# print meaningfullist

def maketextfile(processeddata,filename):
	filename = filename.replace(" ", '_')
	nameHandle = open(filename,'w')
	corpus = processeddata
	for data in corpus:
		nameHandle.write(data.encode('ascii','ignore')+'\n')
		# nameHandle.write('\n')
	nameHandle.close()


# fileHandle = open('Demolinks.txt','r')
# LoL = fileHandle.readlines()
# # print LoL

# for page in LoL:
# 	makecontent(page.rstrip('\n'))

makecontent('http://www.storyit.com/Classics/Stories/dogreflect.htm')
