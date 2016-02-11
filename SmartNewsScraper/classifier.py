'''
The entire classification process is here.
'''
# coding=utf-8
import json	
import nltk
from nltk.corpus import indian
from nltk.corpus import names
from nltk.tokenize import sent_tokenize
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import RegexpTokenizer
import ner
from train_classifier import *
import re
import requests
import settings
import urllib2

#======================================================================================


#======================================================================================


def relevance_features(doc):
	print "relfeatures"
	print doc[:10]
	features={}
	#print doc
	#Test 1 : Has synonyms of  NIT Warangal
	features['contains synonym']='false'
	for word in synonyms:
		if word in doc:
			features['contains synonym']='true'
			break

	#Test 2 : Has a person name that appears in Almabase's DB
	count=0
	names=ner.get_names(data)
	count=ner.query_db(names)
	print 'count is {}'.format(count)

	# if count==0:
	# 	features['hasAlumnus']='none'
	# elif count<=3:
	# 	features['hasAlumnus']='medium'
	# elif count>3:
	# 	features['hasAlumnus']='high'
	# print count

	#Test 3: Bag of words approach
	tokenizer = RegexpTokenizer(r'\w+')
	document_words=tokenizer.tokenize(doc)
	for word in word_features:
		if word.lower() in document_words:
			print "{} is present".format(word)
		features['contains({})'.format(word.lower())] = (word in document_words)
	return features

#===================================================================================

def init_classifier():
	global nbclassifier
	nbclassifier=train_data()

def classify(data):
	result=nbclassifier.classify(relevance_features(data))
	print 'classified as {}'.format(result)
	return result 

	

