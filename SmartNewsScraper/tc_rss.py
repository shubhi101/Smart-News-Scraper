import requests
import feedparser
from bs4 import BeautifulSoup

url="http://feeds.feedburner.com/TechCrunch/"
items=feedparser.parse(url);

def process_url(url):
	#request for url
	#do keyword and entity extraction using NLTK
	#match keywords against existing dictionary of keywords - how do we save the dictionary? In db? 
	#add new keywords to dictionary
	#using keywords as attributes, classify the article-figure out the algo and the attributes to be used



for item in items['entries']:
	soup=BeautifulSoup(item['summary'])
	title=item['title']
	link=item['link']
	pubdate=item['published']
	intro=soup.get_text()
	print(title)
	print(link)
	print(pubdate)
	print(intro)

	#simple db consisting of these 4 columns as of now
	#Store these 4 things in db

	#Check from db if article has already been visited, if yes ignore it
	#else process the article
	process_url(link)






