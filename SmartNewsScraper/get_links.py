'''
Reads Available RSS Feeds to get links of all recent articles in all specified magazines

'''

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from email.Utils import formatdate
from email.utils import parsedate
import datetime
import feedparser
import settings
import time

site_url=["","http://feeds.bbci.co.uk/news/system/latest_published_content/rss.xml","http://feeds.feedburner.com/TechCrunch/","http://yourstory.com/feed/","http://economictimes.indiatimes.com/News/rssfeeds/1715249553.cms"]
site_file=["","bbc.txt","techcrunch.txt","yourstory.txt","et.txt"]
last_seen=""

def get_last_seen():
	f=open("last_seen.txt",'r')
	t=parsedate(f.read())
	last_seen=datetime.datetime(*t[:6])
	print last_seen
	f.close()

def set_last_seen():
	ts=time.time()
	curr=formatdate(time.time())
	f=open("last_seen.txt",'w')
	f.seek(0)
	f.truncate()
	f.write(curr)
	f.close()

def more_recent_than(curr,last):
	t=parsedate(curr)
	d1=datetime.datetime(*t[:6])
	type(d1)
	return d1>last



def write_all_links():
	for i in range(1,5):
		f=open(site_file[i],'w')
		f.seek(0)
		f.truncate()
		items=feedparser.parse(site_url[i])
		for item in items['entries']:
			if (item['published'],last_seen):
				f.write(item['link'].encode('utf-8'))
				f.write("||")
				f.write(item['title'].encode('utf-8'))
				f.write("||")
				f.write(item['published'].encode('utf-8'))
				f.write("\n")
		f.close()


get_last_seen()
write_all_links()
set_last_seen()
