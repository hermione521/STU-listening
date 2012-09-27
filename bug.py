# >_< coding: utf-8 >_<
import urllib2, os
from datetime import date, timedelta
import MySQLdb as mdb

def oldDate(): 
	cur.execute('select count(*) from BBC')
	num = cur.fetchone()
	if num[0] == 0:
		return date(2007, 11, 14) #available after 20071115
	cur.execute('select date from BBC where id = %d' % num[0]);
	old = cur.fetchone()
	return old[0]

def update(url, Id, Title):
	cur.execute('select maxId from BBCinfo')
	maxId = cur.fetchone()[0]
	if Id <= maxId:
		return False
	response = urllib2.urlopen(url)
	page = response.read()
	page = page.decode('GBK').encode('utf-8')
	end = page.find('.mp3" target="_blank">') + 4
	start = page[:end].rfind('http://')
	downURL = page[start : end]
	fileStart = page[:end].rfind('/') + 1
	fileName = page[fileStart : end]
	day = date((ord(page[fileStart])-48)*1000 + (ord(page[fileStart+1])-48)*100 + (ord(page[fileStart+2])-48)*10 + (ord(page[fileStart+3])-48), (ord(page[fileStart+4])-48)*10 + (ord(page[fileStart+5])-48), (ord(page[fileStart+6])-48)*10 + (ord(page[fileStart+7])-48))
	cur.execute('insert into BBC (indexID, date, title, fileName) values (%d, \'%s\', \'%s\', \'%s\')' % (Id, day.isoformat(), Title, fileName))
	con.commit()
	res2 = urllib2.urlopen(downURL)
	data = res2.read()
	open(os.path.join(os.path.abspath("./download/"), fileName), 'wb').write(data)
	return True

def str2num(numStr):
	ans = 0
	for i in range(len(numStr)):
		ans += (ord(numStr[i]) - 48) * (10 ** (len(numStr) - i - 1))
	return ans

def searchPage(pageStr):
	response = urllib2.urlopen(pageStr)
	page = response.read()
 	page = page.decode('GBK').encode('utf-8')
	searchStr = 'html" target="_blank">BBC'
	for i in range(25):
		urlEnd = page.find(searchStr) + 4
		urlStart = page[:urlEnd].rfind('"/') + 1
		titleStart = urlEnd + 22
		titleEnd = titleStart + page[titleStart : ].find('</a>')
		Id = str2num(page[page[:urlEnd].rfind('/') + 1 : urlEnd - 5])
		if not update('http://www.hxen.com' + page[urlStart : urlEnd], Id, page[titleStart : titleEnd]):
			return False
		page = page[titleEnd:]
	return True

def search():
	indexURL = 'http://www.hxen.com/englishlistening/bbc/index.html'
	response = urllib2.urlopen(indexURL)
	page = response.read()
	page = page.decode('GBK').encode('utf-8')
	start = page.find('<b>1/') + 5
	end = start + page[start:].find('<')
	totle = str2num(page[start : end])
	firstEnd = page.find('.html" target="_blank">BBC')
	firstStart = page[:firstEnd].rfind('/') + 1
	firstId = str2num(page[firstStart : firstEnd])
	flag = True
	i = 1
	while flag and i < totle:
		if i == 1:
			pageStr = 'http://www.hxen.com/englishlistening/bbc/index.html'
		else:
			pageStr = 'http://www.hxen.com/englishlistening/bbc/index_%d.html' % i
		flag = searchPage(pageStr)
		i += 1
	#con = mdb.connect('localhost', 'ganyue', 'stulistening', 'listening');
	#cur = con.cursor()
 	cur.execute('update BBCinfo set maxId=%d' % firstId)

if __name__ == '__main__':
	con = mdb.connect('localhost', 'ganyue', 'stulistening', 'listening');
	cur = con.cursor()
	cur.execute('select count(*) from BBCinfo')
	con.commit()
	miao = cur.fetchone()
	if miao[0] == 0:
		cur.execute('insert into BBCinfo (maxId) values (190887)')
	search()
