'''
This module contains functions to the article object and finds all person and org names in it.
It then queries Almabase's db to return the count of distinct names it found in the database.
'''
# coding=utf-8
import json	
import nltk
from nltk.corpus import indian
from nltk.corpus import names
from nltk.tokenize import sent_tokenize
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import RegexpTokenizer
import re
import requests
import settings
import urllib2

endpoint="http://www.nitwaa.in/api/search?q="


def get_names(data):
	names=[]
	for sent in nltk.sent_tokenize(doc):
	    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
	        if hasattr(chunk, 'node'):
	            if chunk.node=='PERSON':
	            	leaf=chunk.leaves()[0]
	            	name = ' '.join(c[0] for c in chunk.leaves())
	            	names.append(name)
	return names


def is_alumnus():
	print "in isalumnus"
	tokens=name.split(" ")
	str="+"
	name=str.join(tokens)
	print name
	url="http://www.nitwaa.in/api/search?q="
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie','sessionid=sedtusafpwf5eqx6abw5rx6co2rte81o'))
	url+=name
	url1=url+"+nit+warangal"
	url2=url+"+rec+warangal"
	# a = opener.open("http://www.nitwaa.in/api/user_status").read()
	try:
		count=0
		a = opener.open(url1).read()
		
		user_array1 = json.loads(a)
		if user_array1['status']=='success':
			count += user_array1['data']['total_results']
		
		b=opener.open(url2).read()
		user_array2= json.loads(b)
		if user_array2['status']=='success':
			count+= user_array2['data']['total_results']
		
		print count
		return count>0	
	except :
		pass	