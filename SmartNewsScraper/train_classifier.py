'''
This file prepares training and testing set for naive bayes classifier, trains the classifier and
shows accuracy of the classifier.
'''
# coding=utf-8
from classifier import *
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

def train_data():
	print "inside train_data\n"
	fh_syn=open("synonyms.txt","r")
	settings.synonyms=fh_syn.read().split('\n')
	fh_syn.close()

	fh_wf=open("word_features.txt","r")
	words=fh_wf.read().split('\n')
	for w in words:
		settings.word_features.append(w.lower())
	fh_wf.close()

	documents=[]

	rel=open("is_relevant.txt","r").read()
	notrel=open("not_relevant.txt").read()

	##Cleaning training data set
	for r in rel.split('\n'):
		if len(r)>0:
			documents.append((r,"rel"))

	for r in notrel.split('\n'):
		if len(r)>0:
			documents.append((r,"notrel"))


	featuresets = [(relevance_features(word.decode('utf-8')),category) for (word,category) in documents]
	random.shuffle(featuresets)
	training_set = featuresets[:20]
	testing_set =  featuresets[20:]

	nbclassifier = nltk.NaiveBayesClassifier.train(training_set)
	print("Original Naive Bayes Algo accuracy percent:",(nltk.classify.accuracy(classifier,testing_set))*100)
	nbclassifier.show_most_informative_features(5)
	return nbclassifier

#=============================================================================================================
