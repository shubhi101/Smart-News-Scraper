'''
This script fetches articles by making http request to the corresponding url and getting the details
like Title, Link, Content and Pubdate
It is also a master script that calls other functions to classify data
'''
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from classifier import *
from email.Utils import formatdate
from email.utils import parsedate
import datetime
import feedparser
from ner import *
import requests
import time
import settings

site_class=["","story-body__inner","article-entry text","ys_post_content text",""]
site_file=["","bbc.txt","techcrunch.txt","yourstory.txt","et.txt"]

def process_url(i):
	r=requests.get(article['Link'])
	data=""
	strainer = SoupStrainer(attrs={'class': site_class[i]})
	soup = BeautifulSoup(r.content, parse_only=strainer)
	if(i==4):
		sections=soup.find_all('div', attrs={'class': 'section1'})
		for section in sections:
			paragraph=section.find('div',attrs={'class': 'Normal'})
			article['Content']+=paragraph.text
	else:
		paragraphs=soup.find_all("p")
		for para in paragraphs:
			article['Content']+=para.text


def get_articles(site):
	f=open(site_file[i],'r')
	articles=f.read().split('\n')
	return articles

def prepare_article(a):
	t=a.split("||")
	settings.article['Link']=t[0]
	settings.article['Title']=t[1]
	settings.article['Pubdate']=t[2]
	return settings.article
			

#==============================================================================
settings.init()
init_classifier()
for site in range(1,5):
	articles=get_articles(site)
	for a in articles:
		article=prepare_article(a)
		process_url(site)
		result=classify(article['Content'])
		print result





